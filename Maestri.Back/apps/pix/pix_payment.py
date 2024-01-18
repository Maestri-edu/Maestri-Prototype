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
            debtor=Debtor(
                id_code=request.payer_id, name=request.payer_name, type=PersonType.PF
            ),
            value=Value(request.payment_value, 1),
            calendar=Calendar(request.expire_seconds),
            key="key",
            solicitation=request.solicitation,
        )

        return self._pay.emit_payment(payment)
