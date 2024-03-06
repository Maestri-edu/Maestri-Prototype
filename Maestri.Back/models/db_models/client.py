from dataclasses import dataclass
from enum import Enum
from datetime import datetime
from typing import Union
from .personal_data import PersonalData
from .user import User


class ClientStatus(Enum):
    financial_pending = 1
    data_pending = 2
    active = 3


class ClientType(Enum):
    lead = 1
    student = 2


@dataclass(order=True)
class Client:
    id: int
    registration_date: datetime
    user: Union[User, int]
    personal_data: Union[PersonalData, int, None]
    status_id: ClientStatus
    type_id: ClientType
