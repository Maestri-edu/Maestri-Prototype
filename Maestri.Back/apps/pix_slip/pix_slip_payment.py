from common.contracts.pix_slip.create_pix_slip_payment import CreatePixSlipPayment
from common.enums.person_enums import PersonType, UF
from models.common.payer_model import PayerModel, Telephone, Address
from models.pix_slip.pix_slip_payment_model import PixSlipPaymentModel
from services.pix_slip.pix_slip_service import PixSlipService


class PixSlipPayment:
    _pix_slip: PixSlipService

    def __init__(self, pix_slip: PixSlipService):
        self._pix_slip = pix_slip

    def create_payment(self, request: CreatePixSlipPayment):
        payment = PixSlipPaymentModel(
            "80",
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
                    "cep",
                    "complete Adress",
                    UF.PR,
                    "city",
                    "neighborhood",
                    "ab1",
                    "complement",
                ),
            ),
        )

        return self._pix_slip.emit_payment(payment)
