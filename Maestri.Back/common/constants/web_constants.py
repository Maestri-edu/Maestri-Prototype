BANK_BASE_URL = "https://cdpj.partners.bancointer.com.br"


class URL:
    value: str

    def __init__(self, value: str):
        self.value = value


class WebConstants:
    OAUTH_TOKEN_REQUEST_URL = URL(BANK_BASE_URL + "/oauth/v2/token")
    PIX_PAYMENT_URL = URL(BANK_BASE_URL + "/pix/v2/cob")
    PIX_SLIP_PAYMENT_URL = URL(BANK_BASE_URL + "/cobranca/v3/cobrancas")


class Hooks:
    PIX = URL(BANK_BASE_URL + "/pix/v2/webhook")
    PIX_SLIP = URL(BANK_BASE_URL + "/cobranca/v3/cobrancas/webhook")


class Util:
    @staticmethod
    def add_url_key(url: URL, key: str):
        return URL(url.value + f"/{key}")
