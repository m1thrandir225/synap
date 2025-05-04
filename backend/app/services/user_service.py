from typing import Optional
from datetime import datetime
from models import CreateUserDTO, UpdateUserDTO, UpdateUserPasswordDTO
from repositories import UserRepository
import bcrypt
from pydantic import EmailStr
from fastapi import HTTPException


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user(self, user_data: CreateUserDTO) -> dict:
        # Check if the email already exists
        if self.user_repo.get_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already in use.")

        # Hash the password
        hashed_password = self.hash_password(user_data.password)

        # Prepare user data for saving
        user_data_dict = user_data.model_dump
        user_data_dict["password"] = hashed_password
        user_data_dict["created_at"] = datetime.now(
            datetime.timezone.utc
        )  # Add created_at

        # Save the user to the repository
        new_user = self.user_repo.create(user_data_dict)

        # Return the newly created user without the password
        return {key: new_user[key] for key in new_user if key != "password"}

    def update_user(self, user_id: str, update_data: UpdateUserDTO) -> dict:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        # Update only the fields that were provided in the DTO
        update_data_dict = update_data.model_dump(exclude_unset=True)

        if "email" in update_data_dict:
            if self.user_repo.get_by_email(update_data_dict["email"]):
                raise HTTPException(status_code=400, detail="Email already in use.")

        # Update the user's details in the repository
        updated_user = self.user_repo.update(user_id, update_data_dict)

        # Return the updated user data without the password
        return {key: updated_user[key] for key in updated_user if key != "password"}

    def update_password(
        self, user_id: str, password_data: UpdateUserPasswordDTO
    ) -> dict:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        # Verify the old password
        if not self.verify_password(password_data.old_password, user["password"]):
            raise HTTPException(status_code=400, detail="Incorrect old password.")

        # Hash the new password
        new_hashed_password = self.hash_password(password_data.new_password)

        # Update the password in the repository
        updated_user = self.user_repo.update(user_id, {"password": new_hashed_password})

        # Return the updated user data without the password
        return {key: updated_user[key] for key in updated_user if key != "password"}

    def delete_user(self, user_id: str) -> dict:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        # Delete the user from the repository
        self.user_repo.delete(user_id)

        # Return a confirmation message (or simply return a success response)
        return {"message": f"User has been successfully deleted."}

    def hash_password(self, password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )
