from Common.Constants.WebConstants import URL
from Common.Contracts.WebHooks.CreatePixSlipWebHook import CreatePixSlipWebHook
from Common.Contracts.WebHooks.CreatePixWebHook import CreatePixWebHook
from Services.Hooks.WebHooks import WebHooks

class HookController():

    _hook: WebHooks

    def __init__(self, hook: WebHooks):
        self._hook = hook

    def create_hook_pix(self, data: CreatePixWebHook):
        response = self._hook.create_pix_hook(URL(data.hook_url), "pix-key")
        return response

    def create_hook_pix_slip(self, data: CreatePixSlipWebHook):
        response = self._hook.create_pix_slip_hook(URL(data.hook_url))
        return response
