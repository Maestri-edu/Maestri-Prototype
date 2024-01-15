from services.pix.pix_service import PixService
from services.pix.pix_hook_service import PixHookService
from services.common.default_request import DefaultRequest
from services.token.auth import Auth


class PixServiceFactory:
    @staticmethod
    def create() -> PixService:
        dr = DefaultRequest()
        auth = Auth(dr)
        return PixService(dr, auth)

    @staticmethod
    def create_options(dr: DefaultRequest, auth: Auth) -> PixService:
        return PixService(dr, auth)


class PixHookServiceFactory:
    @staticmethod
    def create() -> PixHookService:
        dr = DefaultRequest()
        auth = Auth(dr)
        return PixHookService(dr, auth)

    @staticmethod
    def create_options(dr: DefaultRequest, auth: Auth) -> PixHookService:
        return PixHookService(dr, auth)
