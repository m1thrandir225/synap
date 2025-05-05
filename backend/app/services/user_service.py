from typing import Dict
from datetime import datetime, timezone
from app.database import User
from app.models import CreateUserDTO, UpdateUserDTO, UpdateUserPasswordDTO
from app.repositories import UserRepository
from fastapi import HTTPException
from app.security import generate_password_hash, verify_password


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user_email(self, email: str) -> User | None:
        return self.user_repo.get_by_email(email)

    def get_user_id(self, id: str) -> User | None:
        return self.user_repo.get_by_id(str(id))

    def create_user(self, user_data: CreateUserDTO) -> User:
        # Check if the email already exists
        if self.user_repo.get_by_email(user_data.email):
            raise HTTPException(status_code=400, detail="Email already in use.")

        hashed_password = generate_password_hash(user_data.password)

        user_data_dict = user_data.model_dump()
        user_data_dict["password"] = hashed_password
        user_data_dict["updated_at"] = datetime.now(timezone.utc)

        new_user = self.user_repo.create(user_data_dict)

        return new_user

    def update_user(self, user_id: str, update_data: UpdateUserDTO) -> User:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        update_data_dict = update_data.model_dump(exclude_unset=True)

        if "email" in update_data_dict:
            if self.user_repo.get_by_email(update_data_dict["email"]):
                raise HTTPException(status_code=400, detail="Email already in use.")

        updated_user = self.user_repo.update(user_id, update_data_dict)
        if not updated_user:
            raise HTTPException(status_code=500, detail="Error updating user")

        # Return the updated user data without the password
        return updated_user

    def update_password(
        self, user_id: str, password_data: UpdateUserPasswordDTO
    ) -> User:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        if not verify_password(password_data.old_password, str(user.password)):
            raise HTTPException(status_code=400, detail="Incorrect old password.")

        new_hashed_password = generate_password_hash(password_data.new_password)

        updated_user = self.user_repo.update(user_id, {"password": new_hashed_password})

        if not updated_user:
            raise HTTPException(
                status_code=500, detail="There was an error upadting your password"
            )

        return updated_user

    def delete_user(self, user_id: str) -> Dict[str, str]:
        user = self.user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found.")

        self.user_repo.delete(user_id)

        return {"message": "User has been successfully deleted."}
