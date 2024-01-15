from common.constants.web_constants import URL, Hooks
from common.enums.request_type import RequestType
from services.common.default_request import DefaultRequest
from services.token.auth import Auth


class PixSlipHookService:
    _dr: DefaultRequest
    _auth: Auth

    def __init__(self, dr: DefaultRequest, auth: Auth):
        self._dr = dr
        self._auth = auth

    def create_webhook(self, hook_url: URL):
        # HEADER - needs bank account
        response = self._dr.type_request(
            RequestType.PUT,
            Hooks.PIX_SLIP,
            self._auth.get_auth_header(),
            {"webhookUrl": hook_url.value},
        )

        return response
