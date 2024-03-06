from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from models.db_models.charge import ChargeSituation


class PaymentStatus(Enum):
    payed = "RECEBIDO"
    unpayed = "A_RECEBER"
    marked_as_payed = "MARCADO_RECEBIDO"
    late = "ATRASADO"
    canceled = "CANCELADO"
    expired = "EXPIRADO"


_convert = {
    PaymentStatus.payed.value: ChargeSituation.recebido,
    PaymentStatus.unpayed.value: ChargeSituation.a_receber,
    PaymentStatus.marked_as_payed.value: ChargeSituation.marcado_recebido,
    PaymentStatus.late.value: ChargeSituation.atrasado,
    PaymentStatus.canceled.value: ChargeSituation.cancelado,
    PaymentStatus.expired.value: ChargeSituation.expirado,
}


class PaymentStatusDict:

    @staticmethod
    def convert_to_charge_situation(status: str) -> ChargeSituation:
        return _convert[status]


@dataclass
class PixSlipPaymentResponse:
    solicitation_code: str
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
            solicitation_code=data["codigoSolicitacao"],
            account_number=data["seuNumero"],
            status=data["situacao"],
            received_datetime=datetime.fromisoformat(data["dataHoraSituacao"]),
            received_value=data["valorTotalRecebido"],
            payment_origin=data["origemRecebimento"],
            bank_number=data["nossoNumero"],
            bar_code=data["codigoBarras"],
            typed_code=data["linhaDigitavel"],
            txid=data["txid"],
            simple_pix_code=data["pixCopiaECola"],
        )

    def json_request_body(self):
        return {
            "codigoSolicitacao": self.solicitation_code,
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
