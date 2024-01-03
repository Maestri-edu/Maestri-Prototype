from datetime import datetime
from email.policy import default
from flask import Flask, jsonify, request
from Common.Constants.WebConstants import URL
from Common.Enums.PersonEnums import PersonType, UF
from Model.Client.ClientTokenClass import ClientTokenClass
from Model.Payment.PayerModel import PayerModel, Telephone, Address
from Model.Payment.PixPaymentModel import PixPaymentModel, Debtor, Calendar, Value
from Model.Payment.PixPaymentSlipModel import PixPaymentSlipModel
from Services.Common.DefaultRequest import DefaultRequest
from Services.Hooks.WebHooks import WebHooks
from Services.Payment.PaymentRequest import PaymentRequest
from Services.Tokens.OAuth import OAuth

app = Flask(__name__)

default_request = DefaultRequest()
token = ClientTokenClass()
auth = OAuth(default_request, token)
pay = PaymentRequest(default_request, auth)
hook = WebHooks(default_request, auth)

@app.route('/ok')
def get_token2():
    result = auth.get_oauth_bearer_token()
    print(result)
    return ""

@app.route('/ok2')
def get_pix2():
    
    payment = PixPaymentModel(
        Debtor("Jonas", "Id 10092283228"),
        Value(50.50, 1),
        Calendar(10),
        "key",
        "solicitation")

    result = pay.emit_pix_payment(payment)
    
    return ""

@app.route('/ok3')
def get_pix_slip():
    payment = PixPaymentSlipModel(
        '80',
        33.00,
        datetime.today(),
        3,
        PayerModel(
            "9000", 
            "name",
            "email",
            PersonType.PF,
            Telephone("ddd", "number"),
            Address(
                "cep", "complete Adress",
                UF.PR,
                "city",
                "neighborhood",
                "ab1",
                "complement")
            )
        )
    
    result = pay.emit_pix_slip_payment(payment)
    
    return "sin"

@app.route("/hook_pix")
def hook_pix():
    response = hook.create_pix_hook(URL("test-url.com"), "pix-key")
    return "hook_pix"

@app.route("/hook_pix_slip")
def hook_pix_slip():
    response = hook.create_pix_slip_hook(URL("test-url.com"))
    return "hook_pix_slip"

app.run(port=5000, host='localhost', debug=True)
