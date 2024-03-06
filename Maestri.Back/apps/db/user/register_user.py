from typing import Optional
from persistence.repositories.user_repository import UserRepository, User, PersonalData
from models.db_models.user import UserStatus, UserType
from dataclasses import dataclass
from common.helper.datetime_provider import DatetimeProvider as dt


@dataclass(frozen=True, order=True)
class RegisterUserCommand:
    username: str
    password: str
    personal_data: Optional[PersonalData]


class RegisterUser:
    _user_repository: UserRepository

    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def register(self, command: RegisterUserCommand):

        user = User(
            id=0,
            username=command.username,
            password=command.password,
            creation_date=dt.now(),
            personal_data=None,
            status_id=UserStatus.active,
            type_id=UserType.user,
        )

        self._user_repository.insert(user)
