from common.constants.web_constants import URL, Hooks, Util
from common.enums.request_type import RequestType
from services.common.default_request import DefaultRequest
from services.token.auth import Auth


class PixHookService:
    _dr: DefaultRequest
    _auth: Auth

    def __init__(self, dr: DefaultRequest, auth: Auth):
        self._dr = dr
        self._auth = auth

    def create_webhook(self, hook_url: URL, pix_key: str):
        response = self._dr.type_request(
            RequestType.PUT,
            Util.add_url_key(Hooks.PIX, pix_key),
            self._auth.get_auth_header(),
            {"webhookUrl": hook_url.value},
        )
        return response
