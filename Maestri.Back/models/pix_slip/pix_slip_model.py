from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class PixSlipModel:
    solicitation_code: str
    account_number: str
    status: str
    emission_date: date
    due_date: date
    status_date: date
    received_value: float
    payment_origin: str
    bar_code: str
    typed_code: str
    txid: str
    simple_pix_code: str

    @staticmethod
    def create(data: dict):
        return PixSlipModel(
            solicitation_code=data["codigoSolicitacao"],
            account_number=data["seuNumero"],
            status=data["situacao"],
            emission_date=datetime.fromisoformat(data["dataEmissao"]),
            due_date=PixSlipModel.str_to_date(data["dataVencimento"]),
            status_date=PixSlipModel.str_to_date(data["dataSituacao"]),
            received_value=data["valorTotalRecebido"],
            payment_origin=data["origemRecebimento"],
            bar_code=data["codigoBarras"],
            typed_code=data["linhaDigitavel"],
            txid=data["txid"],
            simple_pix_code=data["pixCopiaECola"],
        )

    @staticmethod
    def str_to_date(data) -> date:
        return datetime.strptime(data, "%Y-%m-%d").date()
