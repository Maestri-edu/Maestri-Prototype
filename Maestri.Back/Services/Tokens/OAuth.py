from Model.Client.ClientTokenClass import ClientTokenClass
from Common.Constants.WebConstants import WebConstants as wc
from Services.Common.DefaultRequest import DefaultRequest

class OAuth:
        
    _dr: DefaultRequest
    _token: ClientTokenClass

    def __init__(self, dr: DefaultRequest, token: ClientTokenClass):
        self._dr = dr
        self._token = token

    def get_oauth_token(self):

        request_body = (
            f"client_id=<{self._token.id}>&client_secret=<{self._token.secret}>"
            "&scope=extrato.read boleto-cobranca.read boleto-cobranca.write pagamento-boleto.write pagamento-boleto.read pagamento-darf.write cob.write cob.read cobv.write cobv.read pix.write pix.read webhook.read webhook.write payloadlocation.write payloadlocation.read pagamento-pix.write pagamento-pix.read webhook-banking.write webhook-banking.read"
            "&grant_type=client_credentials"
            )
        
        response = self._dr.post_request (
            wc.OAUTH_TOKEN_REQUEST_URL,
            {"Content-Type": "application/x-www-form-urlencoded"},
            request_body
            )
        
        #token = response.json().get("access_token")
        return "token"

    def get_oauth_bearer_token(self):
        token = self.get_oauth_token()
        return f"Bearer {token}"

    def get_standart_header(self):
        return {
                    "Content-Type": "application/x-www-form-urlencoded"
                }
    
    def get_standart_header_Bearer(self):
        return {
                    "Content-Type": "application/x-www-form-urlencoded", 
                    "Authorization": self.get_oauth_bearer_token()
                }