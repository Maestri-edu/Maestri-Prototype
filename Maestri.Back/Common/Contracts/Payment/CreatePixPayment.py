from dataclasses import dataclass

@dataclass(frozen = True, order = True)
class CreatePixPayment():
    payment_value: float
    payer_id: str
    payer_name: str
    expire_seconds: int
    solicitation: str

    @staticmethod
    def create(data: dict):
        return CreatePixPayment(
            data["payment_value"],
            data["payer_name"],
            data["payer_id"],
            data["expire_seconds"],
            data["solicitation"]
        )