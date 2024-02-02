from common.enums.request_type import RequestType
from common.constants.web_constants import WebConstants as wc
from models.pix_slip.pix_slip_payment_model import PixSlipPaymentModel
from services.common.default_request import DefaultRequest
from services.token.auth import Auth


class PixSlipService:
    _dr: DefaultRequest
    _auth: Auth

    def __init__(self, dr: DefaultRequest, auth: Auth):
        self._dr = dr
        self._auth = auth

    def emit_payment(self, pix_slip_payment: PixSlipPaymentModel):
        response = self._dr.type_request(
            RequestType.POST,
            wc.PIX_SLIP_PAYMENT_URL,
            self._auth.get_auth_header(),
            pix_slip_payment.json_request_body(),
        )

        return response
