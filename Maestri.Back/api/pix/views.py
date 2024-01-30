from result import Ok, Err
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.pix.pix_payment import PixPayment
from common.contracts.pix.create_pix_payment import CreatePixPayment
from common.contracts.pix.pix_payment_response import PixPaymentResponse
from common.factories.pix_factory import PixServiceFactory


@api_view(["POST"])
def create_payment(request):
    request_data = CreatePixPayment.create(request.data)
    pix_payment = PixPayment(PixServiceFactory.create())
    result = pix_payment.create_payment(request_data)
    match result:
        case Ok(success):
            return Response(success)
        case Err(error):
            return Response(status=error.status_code, data=error.data)


@api_view(["POST"])
def payment_response(request):
    response = []
    for data in request.data:
        request_data = PixPaymentResponse.create(data)
        response.append(request_data.json_request_body())
    return Response(response)


@api_view(["GET"])
def get_payments(request):
    request_data = "get"
    return Response(request_data)


@api_view(["GET"])
def get_payment(request, id: int):
    return Response(f"get_by_id {id}")
