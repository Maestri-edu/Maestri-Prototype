from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.pix_slip.pix_slip_payment import PixSlipPayment
from common.contracts.pix_slip.create_pix_slip_payment import CreatePixSlipPayment
from common.factories.pix_slip_factory import PixSlipServiceFactory


@api_view(["POST"])
def create_payment(request):
    request_data = CreatePixSlipPayment.create(request.data)
    pix_slip_payment = PixSlipPayment(PixSlipServiceFactory.create())
    result = pix_slip_payment.create_payment(request_data)
    return Response(result.request)
