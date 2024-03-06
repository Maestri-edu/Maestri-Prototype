from dataclasses import dataclass
from persistence.repositories.user_repository import UserRepository
from models.db_models.user import User


@dataclass
class GetUserByIdQuery:
    id: int


class GetUserById:
    _user_repository: UserRepository

    def get_user(self, command: GetUserByIdQuery):

        return self._user_repository.select_by_id(command.id)
