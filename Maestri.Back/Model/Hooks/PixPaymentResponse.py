
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

    def json_request_body(self):
        return (
            {
                "endToEndId": self.id,
                "chave": self.key,
                "componentesValor": {
                    "original": {
                        "valor": self.original_value
                    }
                },
                "txid": self.txid,
                "valor": str(self.payment_value),
                "horario": self.payment_datetime,
                "infoPagador": self.payer_info
            }
        )

@dataclass
class PixSlipPaymentResponse:
    charge_code: str
    solicitaion_code: str
    account_number: str
    status: str
    received_datetime: datetime
    received_value: float
    payment_origin: float
    bank_number: float
    bar_code: str
    typed_code : str
    txid: str
    simple_pix_code: str

    def json_request_body(self):
        return (
            {
                "codigoCobranca": self.charge_code,
                "codigoSolicitacao": self.solicitaion_code,
                "seuNumero": self.account_number,
                "situacao": self.status,
                "dataHoraSituacao": self.received_datetime,
                "valorTotalRecebido": self.received_value,
                "origemRecebimento": self.payment_origin,
                "nossoNumero": self.bank_number,
                "codigoBarras": self.bar_code,
                "linhaDigitavel": self.typed_code,
                "txid": self.typed_code,
                "pixCopiaECola": self.simple_pix_code
            }
        )