from src.repository.user_repository import UserRepository

from src.model.user import User


class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def get_all_user(self):
        return self._user_repository.get_all_user()

    def create_user(self, name: str, email: str):
        new_user = User(name, email)

        return self._user_repository.create_user(new_user)