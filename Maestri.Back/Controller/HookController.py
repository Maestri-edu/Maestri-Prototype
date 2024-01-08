from Common.Constants.WebConstants import URL
from Services.Hooks.WebHooks import WebHooks

class HookController():

    _hook: WebHooks

    def __init__(self, hook: WebHooks):
        self._hook = hook

    def create_hook_pix(self):
        response = self._hook.create_pix_hook(URL("hook_pix_test-url.com"), "pix-key")
        return response

    def create_hook_pix_slip(self):
        response = self._hook.create_pix_slip_hook(URL("hook_pix_slip_test-url.com"))
        return response
