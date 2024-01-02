
class URL:
    def __init__(self, value: str):
        self.value = value

class WebConstants:
    BANK_BASE_URL = "https://cdpj.partners.bancointer.com.br"
    OAUTH_TOKEN_REQUEST_URL = URL(BANK_BASE_URL + "/oauth/v2/token")
    PIX_PAYMENT_URL = URL(BANK_BASE_URL + "/pix/v2/cob")
    PIX_SLIP_PAYMENT_URL = URL(BANK_BASE_URL + "/cobranca/v3/cobrancas")
    