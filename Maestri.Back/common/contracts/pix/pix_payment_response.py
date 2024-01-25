from dataclasses import dataclass
from datetime import datetime


@dataclass
class PixPaymentResponse:
    id: str
    key: str
    txid: str
    original_value: float
    payment_value: float
    payment_datetime: datetime
    payer_info: str

    @staticmethod
    def create(data: dict):
        return PixPaymentResponse(
            id=data["endToEndId"],
            key=data["chave"],
            txid=data["txid"],
            original_value=data["componentesValor"]["original"]["valor"],
            payment_value=data["valor"],
            payment_datetime=datetime.fromisoformat(data["horario"]),
            payer_info=data["infoPagador"],
        )

    def json_request_body(self):
        return {
            "endToEndId": self.id,
            "chave": self.key,
            "componentesValor": {"original": {"valor": self.original_value}},
            "txid": self.txid,
            "valor": str(self.payment_value),
            "horario": self.payment_datetime,
            "infoPagador": self.payer_info,
        }
