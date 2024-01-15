from common.contracts.pix.create_pix_payment import CreatePixPayment
from common.enums.person_enums import PersonType
from models.pix.pix_payment_model import PixPaymentModel, Debtor, Value, Calendar
from services.pix.pix_service import PixService


class PixPayment:
    _pay: PixService

    def __init__(self, pay: PixService):
        self._pay = pay

    def create_payment(self, request: CreatePixPayment):
        payment = PixPaymentModel(
            Debtor(request.payer_name, request.payer_id, PersonType.PF),
            Value(request.payment_value, 1),
            Calendar(request.expire_seconds),
            "key",
            request.solicitation,
        )

        return self._pay.emit_payment(payment)
