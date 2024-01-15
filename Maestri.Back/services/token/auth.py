from common.constants.web_constants import WebConstants as wc
from common.secrets.secrets import BANK
from common.enums.request_type import RequestType
from services.common.default_request import DefaultRequest


class Auth:
    _dr: DefaultRequest

    def __init__(self, dr: DefaultRequest):
        self._dr = dr

    def get_auth_token(self):
        request_body = (
            f"client_id=<{BANK.CLIENT_ID}>&client_secret=<{BANK.CLIENT_SECRET}>"
            "&scope=extrato.read boleto-cobranca.read boleto-cobranca.write pagamento-boleto.write pagamento-boleto.read pagamento-darf.write cob.write cob.read cobv.write cobv.read pix.write pix.read webhook.read webhook.write payloadlocation.write payloadlocation.read pagamento-pix.write pagamento-pix.read webhook-banking.write webhook-banking.read"
            "&grant_type=client_credentials"
        )

        response = self._dr.type_request(
            RequestType.POST,
            wc.OAUTH_TOKEN_REQUEST_URL,
            {"Content-Type": "application/x-www-form-urlencoded"},
            request_body,
        )

        # token = response.json().get("access_token")
        return response.token

    def get_standart_header(self):
        return {"Content-Type": "application/x-www-form-urlencoded"}

    def get_auth_header(self):
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {self.get_auth_token()}",
        }
