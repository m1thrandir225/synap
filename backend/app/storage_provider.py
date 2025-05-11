import os
import uuid
from pathlib import Path
import aiofiles
import base64

from fastapi import Depends, UploadFile

from app.database.models.user import User
from app.dependencies import get_current_user

class LocalStorageProvider:
    def __init__(
        self, 
        user: User, 
        upload_dir: str = "uploads"
    ):
        if not user or not hasattr(user, 'id'):
                    raise ValueError("LocalStorageProvider requires a valid User object with an ID.")

        self.user = user
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

        self.user_upload_dir = self.upload_dir / str(self.user.id)
        self.user_upload_dir.mkdir(parents=True, exist_ok=True)



    def list_files(self) -> list[str]:
        """Lists files in the user's specific upload directory."""
        try:
            return [item.name for item in self.user_upload_dir.iterdir() if item.is_file()]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error listing files for user {self.user.id}: {e}")
            return [] 

    async def store_file(
            self, 
            file: UploadFile,
            filename: str = None,
            ) -> str:
        """
        Stores an uploaded file. Optionally takes a filename, otherwise
        generates a unique filename using UUID.

        Args:
            file: The uploaded file object from FastAPI.
            filename: Optional. The desired filename to save the file as.
                      If None, a unique UUID-based filename is generated.

        Returns:
            The actual filename under which the file was saved.
        """
        if filename:
            final_filename = filename
        else:
            file_extension = os.path.splitext(file.filename)[1]
            final_filename = str(uuid.uuid4()) + file_extension

        file_path = self.user_upload_dir / final_filename

        async with aiofiles.open(file_path, "wb") as buffer:
            content = await file.read()
            await buffer.write(content)

        return final_filename  

    def get_file(self, filename: str) -> bytes:
        file_path = self.user_upload_dir / filename
        with open(file_path, "rb") as f:
            return f.read()
        
    def get_file_base64(self, filename: str) -> str:
        """
        Reads the file and returns its content encoded in base64.

        Args:
            filename: Name of the file stored under the user's upload directory.

        Returns:
            Base64-encoded string of the file content.
        """
        file_path = self.user_upload_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"File '{filename}' not found for user {self.user.id}.")

        with open(file_path, "rb") as f:
            file_bytes = f.read()
            encoded = base64.b64encode(file_bytes).decode("utf-8")
            return encoded


    def delete_file(self, filename: str) -> None:
        file_path = self.user_upload_dir / filename
        if file_path.exists():
            file_path.unlink()

    def get_file_path(self, filename: str) -> Path:
         """Gets the full Path object for a file in the user's directory."""
         return self.user_upload_dir / filename
    

def get_local_storage_provider(
    user: User = Depends(get_current_user)
) -> LocalStorageProvider:
    return LocalStorageProvider(user=user)

