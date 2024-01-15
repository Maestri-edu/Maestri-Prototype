from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.pix.pix_payment import PixPayment
from common.enums.request_type import RequestType
from common.contracts.pix.create_pix_payment import CreatePixPayment
from common.contracts.pix.pix_payment_response import PixPaymentResponse
from common.factories.pix_factory import PixServiceFactory


@api_view(["POST"])
def create_payment(request):
    request_data = CreatePixPayment.create(request.data)
    pix_payment = PixPayment(PixServiceFactory.create())
    result = pix_payment.create_payment(request_data)
    return Response(result.request)


@api_view(["GET"])
def get_payments(request):
    request_data = "get"
    return Response(request_data)


@api_view(["GET"])
def get_payment(request, id: int):
    return Response(f"get_by_id {id}")


@api_view(["POST"])
def payment_response(request):
    request_data = PixPaymentResponse.create(request.data)
    return Response(request.data)
