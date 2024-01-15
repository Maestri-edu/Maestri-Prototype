from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class CreatePixSlipPayment:
    payment_value: float
    payer_id: str
    payer_name: str
    due_date: datetime
    due_date_limit: int

    @staticmethod
    def create(data: dict):
        return CreatePixSlipPayment(
            data["payment_value"],
            data["payer_id"],
            data["payer_name"],
            datetime.now(),
            1,
        )
