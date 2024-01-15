from datetime import datetime
from dataclasses import dataclass
from models.common.payer_model import PayerModel


@dataclass
class PixSlipPaymentModel:
    title_number: str
    value: float
    due_date: datetime
    due_date_spare_limit: int
    payer: PayerModel

    def json_request_body(self):
        return {
            "seuNumero": self.title_number,
            "valorNominal": self.value,
            "dataVencimento": self.due_date.strftime("%Y-%m-%d"),
            "numDiasAgenda": self.due_date_spare_limit,
            "pagador": self.payer.json_request_body(),
        }
