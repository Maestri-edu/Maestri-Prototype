from dataclasses import dataclass
from datetime import datetime


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
    typed_code: str
    txid: str
    simple_pix_code: str

    def json_request_body(self):
        return {
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
            "pixCopiaECola": self.simple_pix_code,
        }
