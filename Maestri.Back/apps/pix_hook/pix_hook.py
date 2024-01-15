from common.constants.web_constants import URL
from common.contracts.hook.create_pix_hook import CreatePixWebHook
from services.pix.pix_hook_service import PixHookService


class PixHook:
    _hook: PixHookService

    def __init__(self, hook: PixHookService):
        self._hook = hook

    def create_hook(self, data: CreatePixWebHook):
        response = self._hook.create_webhook(URL(data.hook_url), "pix-key")
        return response
