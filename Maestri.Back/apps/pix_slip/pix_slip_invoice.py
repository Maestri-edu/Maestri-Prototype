from services.pix_slip.pix_slip_service import PixSlipService
from common.contracts.pix_slip.get_pix_slip_invoice import GetPixSlipInvoice


class PixSlipInvoice:

    _pix_slip: PixSlipService

    def __init__(self, pix_slip: PixSlipService):
        self._pix_slip = pix_slip

    def get_pix_slip_invoice(self, request: GetPixSlipInvoice):

        return self._pix_slip.get_payment_invoice(request.payment_id)
