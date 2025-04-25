from fastapi import APIRouter, UploadFile, Depends, HTTPException, status
from fastapi.responses import FileResponse
from typing import List
from pydantic import BaseModel

from app.storage_provider import LocalStorageProvider

class FileInfo(BaseModel):
    filename: str

router = APIRouter(prefix="/files", tags=["Files"])

@router.get("/", response_model=List[FileInfo])
async def list_user_files(
    storage_provider: LocalStorageProvider = Depends(LocalStorageProvider)
):
    """
    Lists all files stored for the current authenticated user.
    Requires authentication because LocalStorageProvider depends on the user.
    """
    filenames = storage_provider.list_files()
    return [{"filename": name} for name in filenames]


@router.post("/", status_code=status.HTTP_201_CREATED) 
async def upload_file(
    file: UploadFile,
    storage_provider: LocalStorageProvider = Depends(LocalStorageProvider)
):
    """
    Uploads a new file for the current authenticated user.
    Requires authentication.
    """
    if not file.filename:
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No filename provided")
    
    try:
        saved_filename = await storage_provider.store_file(file, filename=file.filename)
        return {
            "message": "File uploaded successfully",
            "filename": saved_filename,
            "location": router.prefix + "/" + saved_filename
            }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to upload file")


@router.get("/{filename}")
async def get_file(
    filename: str,
    storage_provider: LocalStorageProvider = Depends(LocalStorageProvider)
):
    """
    Retrieves a specific file for the current authenticated user.
    Requires authentication.
    """
    file_path = storage_provider.get_file_path(filename)

    if not file_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    return FileResponse(file_path)

@router.delete("/{filename}")
async def delete_file(
    filename: str,
    storage_provider: LocalStorageProvider = Depends(LocalStorageProvider)
):
    """
    Deletes a specific file for the current authenticated user.
    Requires authentication.
    """
    file_path = storage_provider.get_file_path(filename)

    if not file_path.is_file():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="File not found")

    try:
        storage_provider.delete_file(filename)
        return {"message": f"File '{filename}' deleted successfully"}
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete file")