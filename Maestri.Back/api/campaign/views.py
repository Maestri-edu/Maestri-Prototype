from rest_framework.response import Response
from rest_framework.decorators import api_view
from common.contracts.campaign.create_pix_slip_payment import (
    CreateCampaignPixSlipPayment,
)
from common.factories.pix_slip_payment_factory import PixSlipPaymentFactory
from result import Ok, Err


@api_view(["POST"])
def create_pix_slip_payment(request):
    request_data = CreateCampaignPixSlipPayment.create(request.data)
    pix_slip_payment = PixSlipPaymentFactory.create()
    response = pix_slip_payment.create_payment(request_data)
    match (response):
        case Ok(success):
            return Response(status=(success.status_code), data=success.data)
        case Err(error):
            return Response(status=(error.status_code), data=error.data)

    return Response(request_data.json_request_body())


@api_view(["POST"])
def create_pix_slip_payment_op(request):

    request_data = CreateCampaignPixSlipPayment.create(request.data)
    # return Response(status=400, data=request_data.json_request_body())
    return Response(status=500, data="hello there")
