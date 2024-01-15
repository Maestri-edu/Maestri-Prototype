from common.constants.web_constants import URL
from common.contracts.hook.create_pix_slip_hook import CreatePixSlipWebHook
from services.pix_slip.pix_slip_hook_service import PixSlipHookService


class PixSlipHook:
    _hook: PixSlipHookService

    def __init__(self, hook: PixSlipHookService):
        self._hook = hook

    def create_hook(self, data: CreatePixSlipWebHook):
        response = self._hook.create_webhook(URL(data.hook_url))
        return response
