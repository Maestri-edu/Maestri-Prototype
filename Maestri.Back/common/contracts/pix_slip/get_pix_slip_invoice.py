from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class GetPixSlipInvoice:
    payment_id: str

    @staticmethod
    def create(data: dict):
        return GetPixSlipInvoice(
            payment_id=data["paymentId"],
        )
