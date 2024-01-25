from common.contracts.pix_slip.create_pix_slip_payment import CreatePixSlipPayment
from common.enums.person_enums import PersonType, UF
from models.common.payer_model import PayerModel, Telephone, Address
from models.pix_slip.pix_slip_payment_model import PixSlipPaymentModel
from services.pix_slip.pix_slip_service import PixSlipService
from common.helper.datetime_provider import DatetimeProvider as dt
import datetime


class PixSlipPayment:
    _pix_slip: PixSlipService

    def __init__(self, pix_slip: PixSlipService):
        self._pix_slip = pix_slip

    def create_payment(self, request: CreatePixSlipPayment):
        request_due_date = dt.utc_now() + datetime.timedelta(days=30)

        payment = PixSlipPaymentModel(
            title_number="80",
            value=request.payment_value,
            due_date=request_due_date,
            due_date_spare_limit=7,
            payer=PayerModel(
                id_number=request.payer_id,
                name=request.payer_name,
                email="email",
                type=PersonType.PF,
                telephone=Telephone("ddd", "number"),
                adress=Address(
                    cep_number="cep",
                    complete_adress="complete Adress",
                    uf=UF.PR,
                    city="city",
                    neighborhood="neighborhood",
                    number="ab1",
                    complement="complement",
                ),
            ),
        )

        return self._pix_slip.emit_payment(payment)
