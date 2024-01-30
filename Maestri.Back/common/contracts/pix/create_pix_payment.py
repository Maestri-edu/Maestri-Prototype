from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class CreatePixPayment:
    payment_value: float
    payer_id: str
    payer_name: str
    solicitation: str

    @staticmethod
    def create(data: dict):
        return CreatePixPayment(
            payment_value=data["paymentValue"],
            payer_id=data["payerId"],
            payer_name=data["payerName"],
            solicitation=data["solicitation"],
        )
