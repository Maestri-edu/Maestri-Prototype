from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.campaign.pix_slip_payment import PixSlipPayment
from common.contracts.campaign.create_pix_slip_payment import (
    CreateCampaignPixSlipPayment,
)
from common.factories.pix_slip_factory import PixSlipServiceFactory


@api_view(["POST"])
def create_pix_slip_payment(request):
    request_data = CreateCampaignPixSlipPayment.create(request.data)
    pix_slip_payment = PixSlipPayment(PixSlipServiceFactory.create())
    response = pix_slip_payment.create_payment(request_data)
    return Response(request_data.json_request_body())
