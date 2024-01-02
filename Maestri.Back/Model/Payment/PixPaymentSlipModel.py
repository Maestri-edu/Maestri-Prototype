from dataclasses import dataclass
from Model.Payment.PayerModel import PayerModel
import datetime as dt

@dataclass
class PixPaymentSlipModel:
    number: str
    value: float
    due_date: dt.datetime
    due_date_spare_limit: int
    payer: PayerModel
    
    def json_request_body(self):
        return (
            {
                "seuNumero": self.number,
                "valorNominal": self.value,
                "dataVencimento": str(self.due_date),
                "numDiasAgenda": self.due_date_spare_limit,
                "pagador": self.payer.json_request_body()
            }
        )