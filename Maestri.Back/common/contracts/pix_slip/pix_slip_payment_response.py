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

    @staticmethod
    def create(data: dict):
        return PixSlipPaymentResponse(
            charge_code=data["codigoCobrança"],
            solicitaion_code=data["codigoSolicitacao"],
            account_number=data["seuNumero"],
            status=data["situacao"],
            received_datetime=data["dataHoraSituacao"],
            received_value=data["valorTotalRecebido"],
            payment_origin=data["origemRecebimento"],
            bank_number=data["nossoNumero"],
            bar_code=data["condigoBarras"],
            typed_code=data["linhaDigitavel"],
            txid=data["txid"],
            simple_pix_code=data["pixCopiaECola"],
        )

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
