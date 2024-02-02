from rest_framework.response import Response
from rest_framework.decorators import api_view
from result import Ok, Err
from apps.pix_hook.pix_hook import PixHook
from apps.pix_slip_hook.pix_slip_hook import PixSlipHook
from common.contracts.hook.create_pix_hook import CreatePixWebHook
from common.contracts.hook.create_pix_slip_hook import CreatePixSlipWebHook
from common.factories.pix_factory import PixHookServiceFactory
from common.factories.pix_slip_factory import PixSlipHookServiceFactory


@api_view(["POST"])
def create_hook_pix(request):
    request_data = CreatePixWebHook.create(request.data)
    _pix_hook = PixHook(PixHookServiceFactory.create())
    response = _pix_hook.create_hook(request_data)

    match (response):
        case Ok(success):
            return Response(status=(success.status_code), data=success.data)
        case Err(error):
            return Response(status=(error.status_code), data=error.data)

    return Response(response.request)


@api_view(["POST"])
def create_hook_pix_slip(request):
    request_data = CreatePixSlipWebHook.create(request.data)
    _pix_slip_hook = PixSlipHook(PixSlipHookServiceFactory.create())
    response = _pix_slip_hook.create_hook(request_data)

    match (response):
        case Ok(success):
            return Response(status=(success.status_code), data=success.data)
        case Err(error):
            return Response(status=(error.status_code), data=error.data)

    return Response(response.request)
