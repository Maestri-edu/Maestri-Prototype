from Common.Enums.PersonEnums import PersonType, UF
from Model.Payment.PayerModel import PayerModel, Telephone, Address
from Model.Payment.PixPaymentModel import PixPaymentModel, Debtor, Calendar, Value
from Model.Payment.PixPaymentSlipModel import PixPaymentSlipModel
from Services.Payment.PaymentRequest import PaymentRequest
from Common.Contracts.Payment.CreatePixPayment import CreatePixPayment
from Common.Contracts.Payment.CreatePixSlipPayment import CreatePixSlipPayment

class PaymentController():
    
    _pay: PaymentRequest

    def __init__(self, pay: PaymentRequest):
        self._pay = pay

    def create_pix_payment(self, request: CreatePixPayment):
        
        payment = PixPaymentModel(
            Debtor(request.payer_name, request.payer_id, PersonType.PF),
            Value(request.payment_value, 1),
            Calendar(request.expire_seconds),
            "key",
            request.solicitation)

        return self._pay.emit_pix_payment(payment)

    def create_pix_slip_payment(self, request: CreatePixSlipPayment):

        payment = PixPaymentSlipModel(
            '80',
            request.payment_value,
            request.due_date,
            request.due_date_limit,
            PayerModel(
                request.payer_id,
                request.payer_name,
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
        
        return self._pay.emit_pix_slip_payment(payment)

