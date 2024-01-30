from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class CreatePixSlipPayment:
    payment_value: float
    payer_id: str
    payer_name: str

    @staticmethod
    def create(data: dict):
        return CreatePixSlipPayment(
            payment_value=data["paymentValue"],
            payer_id=data["payerId"],
            payer_name=data["payerName"],
        )
