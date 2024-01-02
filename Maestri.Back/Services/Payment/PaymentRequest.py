from dataclasses import dataclass
from Model.Payment.PixPaymentModel import PixPaymentModel
from Model.Payment.PixPaymentSlipModel import PixPaymentSlipModel
from Services.Common.DefaultRequest import DefaultRequest
from Common.Constants.WebConstants import WebConstants as wc
from Services.Tokens.OAuth import OAuth

class PaymentRequest:
    
    _dr: DefaultRequest
    _auth: OAuth

    def __init__(self, requestHandler: DefaultRequest, auth: OAuth):
        self._dr = requestHandler
        self._auth = auth

    def emit_pix_payment(self, pix_payment: PixPaymentModel):
        
        response = self._dr.post_request(
            wc.PIX_PAYMENT_URL,
            self._auth.get_standart_header_Bearer(),
            pix_payment.json_request_body()
            )
        
        if response.status_code != 200:
            print(f"Oh well... what now?. {response.status_code}")
        
        return response

    def emit_pix_slip_payment(self, pix_slip_payment: PixPaymentSlipModel):
        
        response = self._dr.post_request(
            wc.PIX_SLIP_PAYMENT_URL,
            self._auth.get_standart_header_Bearer(), 
            pix_slip_payment.json_request_body()
            )
        
        if response.status_code != 200:
            print(f"Oh well... what now?. {response.status_code}")
        
        return response