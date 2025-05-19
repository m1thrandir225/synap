import base64
from io import BytesIO
import os
import uuid
from botocore.client import ClientError
from app.database import User, UploadedFile
import boto3
from fastapi import UploadFile

class S3StorageProvider:
    def __init__(
            self,
            user: User,
            bucket_name: str,
            aws_access_key_id: str, 
            aws_secret_access_key: str,
            endpoint_url: str | None = None,
            region_name: str | None = None
    ):
        if not user or not hasattr(user, "id"):
            raise ValueError("S3StorageProvider requires a valid User object with an ID.")

        if not  bucket_name:
            raise ValueError("S3 bucket_name is required")
        if not aws_access_key_id or not aws_secret_access_key:
            raise ValueError("AWS credentials (access_key and secret_access_key) are required.")
        self.user = user
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            endpoint_url=endpoint_url,
            region_name=region_name
        )
        self.user_prefix = f"{str(self.user.id)}"

    def _get_s3_key(self, filename: str) -> str:
        """
        Constructs the S3 object key for a given filename within the user's prefix.
        """
        return f"{self.user_prefix}{filename}"

    def get_full_s3_key_for_file(self, filename_in_s3: str) -> str:
        """Helper to get the full S3 key for a filename relative to user's prefix."""
        return self._get_s3_key(filename_in_s3)

    def list_files(self) -> list[str]:
        """
        Lists files in the user's specific S3 prefix.
        """
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name, Prefix=self.user_prefix
            )
            files = []
            if "Contents" in response:
                for item in response["Contents"]:
                    # Remove the user prefix to get the base filename
                    # Also, S3 lists "folders" (objects ending with /) if they exist,
                    # so we filter them out if we only want files.
                    if not item["Key"].endswith("/"): # Exclude the prefix "folder" itself
                        file_key = item["Key"]
                        # Remove the prefix from the key to get the filename
                        filename = file_key[len(self.user_prefix):]
                        if filename: # Ensure it's not an empty string if key was just the prefix
                             files.append(filename)
            return files
        except ClientError as e:
            print(f"Error listing files for user {self.user.id} in bucket {self.bucket_name}: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred while listing files for user {self.user.id}: {e}")
            return []

    async def store_file(
        self,
        file: UploadFile,
        filename: str | None = None,
    ) -> str:
        """
        Stores an uploaded file in S3.

        Args:
            file: The uploaded file object from FastAPI.
            filename: Optional. The desired filename to save the file as.
                      If None, a unique UUID-based filename is generated.

        Returns:
            The actual filename under which the file was saved in S3 (without the user prefix).
        
        Note:
            The `boto3` S3 client's `upload_fileobj` and `put_object` are synchronous.
            For a fully asynchronous FastAPI application, consider using `aioboto3`
            or running these operations in a thread pool executor.
        """
        if filename:
            final_filename = filename
        else:
            if not file.filename:
                # Fallback if UploadFile has no filename (e.g. from bytes)
                # You might want to enforce a content type or raise an error
                base_name = "file"
                file_extension = ".dat" # Default extension
            else:
                base_name, file_extension = os.path.splitext(file.filename)
            final_filename = str(uuid.uuid4()) + file_extension

        s3_key = self._get_s3_key(final_filename)
        
        try:
            # Read the file content. file.read() is an async operation.
            content = await file.read()
            # Reset the file pointer if it's going to be read again (not strictly necessary for BytesIO)
            await file.seek(0)

            # Use BytesIO to treat the content as a file-like object for boto3
            file_obj = BytesIO(content)
            
            self.s3_client.upload_fileobj(
                Fileobj=file_obj,
                Bucket=self.bucket_name,
                Key=s3_key,
                # You can add ExtraArgs here, e.g., for ContentType
                # ExtraArgs={'ContentType': file.content_type}
            )
            return final_filename
        except ClientError as e:
            print(f"Error uploading file {final_filename} to S3 for user {self.user.id}: {e}")
            raise Exception(f"Could not store file in S3: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during S3 upload for {final_filename}: {e}")
            raise Exception(f"An unexpected error occurred while storing the file: {e}")
    def get_file(self, filename: str) -> bytes:
        """
        Retrieves a file from S3.

        Args:
            filename: Name of the file stored under the user's S3 prefix.

        Returns:
            The file content as bytes.
        
        Raises:
            FileNotFoundError: If the file is not found in S3.
            Exception: For other S3 related errors.
        """
        s3_key = self._get_s3_key(filename)
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=s3_key)
            return response["Body"].read()
        except ClientError as e:
            if e.response["Error"]["Code"] == "NoSuchKey":
                raise FileNotFoundError(
                    f"File '{filename}' not found for user {self.user.id} in bucket {self.bucket_name}."
                )
            else:
                print(f"Error getting file {filename} from S3 for user {self.user.id}: {e}")
                raise Exception(f"Could not retrieve file from S3: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while getting file {filename} for user {self.user.id}: {e}")
            raise Exception(f"An unexpected error occurred while retrieving the file: {e}")


    def get_file_base64(self, filename: str) -> str:
        """
        Reads the file from S3 and returns its content encoded in base64.

        Args:
            filename: Name of the file stored under the user's S3 prefix.

        Returns:
            Base64-encoded string of the file content.
        
        Raises:
            FileNotFoundError: If the file is not found in S3.
            Exception: For other S3 related errors.
        """
        file_bytes = self.get_file(filename) # Reuses get_file which handles FileNotFoundError
        encoded = base64.b64encode(file_bytes).decode("utf-8")
        return encoded

    async def delete_file(self, filename: str) -> None:
        """
        Deletes a file from S3.

        Args:
            filename: Name of the file stored under the user's S3 prefix.
        """
        s3_key = self._get_s3_key(filename)
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=s3_key)
            print(f"File '{s3_key}' deleted successfully from bucket '{self.bucket_name}'.")
        except ClientError as e:
            print(f"Error deleting file {s3_key} from S3 for user {self.user.id}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred while deleting file {s3_key} for user {self.user.id}: {e}")


    def get_file_path(self, filename: str) -> str:
        """
        Gets the S3 object key for a file in the user's "directory".
        This is not a local file path but the key used to identify the object in S3.
        """
        return self._get_s3_key(filename)

    def generate_presigned_url(self, filename: str, expiration: int = 3600) -> str | None:
        """
        Generates a presigned URL to access an S3 object.

        Args:
            filename: Name of the file stored under the user's S3 prefix.
            expiration: Time in seconds for the presigned URL to remain valid. Default 1 hour.

        Returns:
            The presigned URL string, or None if an error occurs.
        """
        s3_key = self._get_s3_key(filename)
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': s3_key},
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            print(f"Error generating presigned URL for {s3_key}: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while generating presigned URL for {s3_key}: {e}")
            return None