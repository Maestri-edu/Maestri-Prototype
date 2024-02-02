from result import Result
from common.constants.web_constants import WebConstants as wc
from common.enums.request_type import RequestType
from models.pix.pix_payment_model import PixPaymentModel
from services.common.default_request import (
    DefaultRequest,
    SuccessResponse,
    ErrorResponse,
)
from services.token.auth import Auth


class PixService:
    _dr: DefaultRequest
    _auth: Auth

    def __init__(self, dr: DefaultRequest, auth: Auth):
        self._dr = dr
        self._auth = auth

    def emit_payment(
        self, pix_payment: PixPaymentModel
    ) -> Result[SuccessResponse, ErrorResponse]:
        response = self._dr.type_request(
            RequestType.POST,
            wc.PIX_PAYMENT_URL,
            self._auth.get_auth_header(),
            pix_payment.json_request_body(),
        )

        return response
