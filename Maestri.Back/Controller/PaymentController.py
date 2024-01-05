from datetime import datetime
from email.policy import default
from Common.Enums.PersonEnums import PersonType, UF
from Model.Payment.PayerModel import PayerModel, Telephone, Address
from Model.Payment.PixPaymentModel import PixPaymentModel, Debtor, Calendar, Value
from Model.Payment.PixPaymentSlipModel import PixPaymentSlipModel
from Services.Payment.PaymentRequest import PaymentRequest

class PaymentController():
    
    _pay: PaymentRequest

    def __init__(self, pay: PaymentRequest):
        self._pay = pay

    def create_pix_payment(self):
        
        payment = PixPaymentModel(
            Debtor("Jonas", "Id 10092283228"),
            Value(50.50, 1),
            Calendar(10),
            "key",
            "solicitation")

        result = self._pay.emit_pix_payment(payment)

        return ""

    def create_pix_slip_payment(self):
        payment = PixPaymentSlipModel(
            '80',
            33.00,
            datetime.today(),
            3,
            PayerModel(
                "9000", 
                "name",
                "email",
                PersonType.PF,
                Telephone("ddd", "number"),
                Address(
                    "cep", "complete Adress",
                    UF.PR,
                    "city",
                    "neighborhood",
                    "ab1",
                    "complement")
                )
            )
        
        result = self._pay.emit_pix_slip_payment(payment)
        
        return "sin"
