from result import Err, Ok
from common.constants.web_constants import WebConstants as wc
from common.enums.request_type import RequestType
from common.helper.datetime_provider import DatetimeProvider as dt
from common.secrets.secrets import BANK
from common.secrets.auth import AuthToken, AuthTokenModel
from services.common.default_request import DefaultRequest
import datetime


class Auth:
    _dr: DefaultRequest

    def __init__(self, dr: DefaultRequest):
        self._dr = dr

    def get_auth_token(self):
        current_token = AuthToken.get_current_auth_token()

        if current_token.IsValid():
            print("current token")
            return current_token.value

        print("new token")
        new_token_response = self.auth_token_request()

        match (new_token_response):
            case Ok(success):
                new_token: str = success.data["access_token"]
                self._save_new_token(new_token)
                return new_token
            case Err(error):
                print("Not good, something is wrong", error.data)
                return current_token.value

    def _save_new_token(self, token_value: str):
        token = AuthTokenModel(
            value=token_value,
            created=dt.utc_now(),
            expire=dt.utc_now() + datetime.timedelta(minutes=30),
        )
        AuthToken.save_new_token(token)

    def auth_token_request(self):
        request_body = (
            f"client_id=<{BANK.CLIENT_ID}>&client_secret=<{BANK.CLIENT_SECRET}>"
            "&scope=extrato.read boleto-cobranca.read boleto-cobranca.write pagamento-boleto.write pagamento-boleto.read pagamento-darf.write cob.write cob.read cobv.write cobv.read pix.write pix.read webhook.read webhook.write payloadlocation.write payloadlocation.read pagamento-pix.write pagamento-pix.read webhook-banking.write webhook-banking.read"
            "&grant_type=client_credentials"
        )

        response = self._dr.type_request(
            RequestType.POST,
            wc.OAUTH_TOKEN_REQUEST_URL,
            self.get_standard_header(),
            request_body,
        )

        return response

    def get_standard_header(self):
        return {"Content-Type": "application/x-www-form-urlencoded"}

    def get_auth_header(self):
        return {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Bearer {self.get_auth_token()}",
        }
