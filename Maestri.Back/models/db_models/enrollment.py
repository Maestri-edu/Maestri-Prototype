from dataclasses import dataclass
from enum import Enum
from typing import Union
from .client import Client
from .course import Course


class EnrollmentStatus(Enum):
    pending_awaiting_registration_fee_payment = 1
    pending_awaiting_documentation = 2
    debtor = 3
    braided = 4
    canceled = 5
    concluded = 6
    active = 7


@dataclass(order=True)
class Enrollment:
    id: int
    number_of_installments: int
    client: Union[Client, int]
    course: Union[Course, int]
    status_id: EnrollmentStatus

    def extract_id(self, model: Union[Client, Course, int]) -> int:

        match (model):
            case Course() | Client():
                return model.id
            case int():
                return model
