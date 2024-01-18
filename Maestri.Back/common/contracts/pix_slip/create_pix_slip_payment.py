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
            payment_value=data["payment_value"],
            payer_id=data["payer_id"],
            payer_name=data["payer_name"],
            due_date=datetime.now(),
            due_date_limit=1,
        )
