from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.pix_slip.pix_slip_payment import PixSlipPayment
from common.contracts.pix_slip.create_pix_slip_payment import CreatePixSlipPayment
from common.contracts.pix_slip.pix_slip_payment_response import PixSlipPaymentResponse
from common.factories.pix_slip_factory import PixSlipServiceFactory
from result import Ok, Err


@api_view(["POST"])
def create_payment(request):
    request_data = CreatePixSlipPayment.create(request.data)
    pix_slip_payment = PixSlipPayment(PixSlipServiceFactory.create())
    response = pix_slip_payment.create_payment(request_data)

    match (response):
        case Ok(success):
            print("here boy!")
            return Response(status=(success.status_code), data=success.data)
        case Err(error):
            print("here boy?")
            return Response(status=(error.status_code), data=error.data)

    return Response(response.request)


@api_view(["POST"])
def payment_response(request):
    response = []
    for data in request.data:
        request_data = PixSlipPaymentResponse.create(data)
        response.append(request_data.json_request_body())

    match (response):
        case Ok(success):
            return Response(status=(success.status_code), data=success.data)
        case Err(error):
            return Response(status=(error.status_code), data=error.data)

    return Response(response)
