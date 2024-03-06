from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, Union
from models.db_models.personal_data import PersonalData


class UserType(Enum):
    user = 1
    promotor = 2
    client = 3
    lead = 4
    student = 5


class UserStatus(Enum):
    pending = 1
    active = 2
    banned = 3
    inactive = 4
    blocked = 5
    financial_block = 6


@dataclass(order=True)
class User:
    id: int
    username: str
    password: str
    creation_date: datetime
    personal_data: Union[PersonalData, int, None]
    status_id: UserStatus
    type_id: UserType

    def extract_id(self, value: Union[PersonalData, int, None]) -> Optional[int]:

        if value is None:
            return value

        if isinstance(value, int):
            return value

        return value.id
