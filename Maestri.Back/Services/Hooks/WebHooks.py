from Common.Constants.WebConstants import URL, Hooks, Util
from Services.Common.DefaultRequest import DefaultRequest
from Services.Tokens.OAuth import OAuth
from Common.Enums.RequestType import RequestType

class WebHooks:
    _dr: DefaultRequest
    _auth: OAuth

    def __init__(self, dr: DefaultRequest, auth: OAuth):
        self._dr = dr
        self._auth = auth

    def create_pix_hook(self, hook_url: URL, pix_key: str):
        
        response = self._dr.type_request(
            RequestType.PUT,
            Util.add_url_key(Hooks.PIX, pix_key),
            self._auth.get_standart_header_Bearer(),
            {
                "webhookUrl": hook_url.value
            }
        )

        return response

    def create_pix_slip_hook(self, hook_url: URL):
        
        #HEADER - needs bank account
        response = self._dr.type_request(
            RequestType.PUT,
            Hooks.PIX_SLIP,
            self._auth.get_standart_header_Bearer(),
            {
                "webhookUrl": hook_url.value
            }
        )
        
        return response
