from services.pix_slip.pix_slip_service import PixSlipService
from services.pix_slip.pix_slip_hook_service import PixSlipHookService
from services.common.default_request import DefaultRequest
from services.token.auth import Auth


class PixSlipServiceFactory:
    @staticmethod
    def create() -> PixSlipService:
        dr = DefaultRequest()
        auth = Auth(dr)
        return PixSlipService(dr, auth)

    @staticmethod
    def create_options(dr: DefaultRequest, auth: Auth) -> PixSlipService:
        return PixSlipService(dr, auth)


class PixSlipHookServiceFactory:
    @staticmethod
    def create() -> PixSlipHookService:
        dr = DefaultRequest()
        auth = Auth(dr)
        return PixSlipHookService(dr, auth)

    @staticmethod
    def create_options(dr: DefaultRequest, auth: Auth) -> PixSlipHookService:
        return PixSlipHookService(dr, auth)
