from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class CreatePixPayment:
    payment_value: float
    payer_id: str
    payer_name: str
    expire_seconds: int
    solicitation: str

    @staticmethod
    def create(data: dict):
        return CreatePixPayment(
            payment_value=data["payment_value"],
            payer_id=data["payer_id"],
            payer_name=data["payer_name"],
            expire_seconds=data["expire_seconds"],
            solicitation=data["solicitation"],
        )
