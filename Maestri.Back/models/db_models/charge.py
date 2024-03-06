from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Union
from models.db_models.enrollment import Enrollment


class ChargeType(Enum):
    enrolment_free = 1
    monthly_payment = 2


class ChargeSituation(Enum):
    atrasado = 1
    a_receber = 2
    cancelado = 3
    expirado = 4
    marcado_recebido = 5
    recebido = 6


@dataclass(order=True)
class Charge:
    id: int
    enrollment: Union[Enrollment, int]
    type_id: ChargeType
    situation_id: ChargeSituation
    solicitation_code: str
    your_number: str
    our_number: str
    received_datetime: datetime
    received_value: float
    payment_origin: str
    bar_code: str
    typed_code: str
    txid: str
    simple_pix_code: str

    def extract_id(self, value: Union[Enrollment, int]) -> int:

        if isinstance(value, Enrollment):
            return value.id

        return value
