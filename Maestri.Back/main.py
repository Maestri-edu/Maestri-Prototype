# from flask import Flask, jsonify, request
# from models.Client.ClientTokenClass import ClientTokenClass
# from Services.Common.DefaultRequest import DefaultRequest
# from Services.Hooks.WebHooks import WebHooks
# from Services.Payment.PaymentRequest import PaymentRequest
# from Services.Tokens.OAuth import OAuth

# from controllers.Hookcontrollers import Hookcontrollers
# from controllers.Paymentcontrollers import Paymentcontrollers

# app = Flask(__name__)

# default_request = DefaultRequest()
# token = ClientTokenClass()
# auth = OAuth(default_request, token)
# pay = PaymentRequest(default_request, auth)
# hook = WebHooks(default_request, auth)

# hook_controllers = Hookcontrollers(hook)
# payment_controllers = Paymentcontrollers(pay)

# @app.route('/ok')
# def get_token2():
#     result = auth.get_oauth_bearer_token()
#     print(result)
#     return ""

# @app.route('/ok2')
# def get_pix2():
#     result = payment_controllers.create_pix_payment()
#     return ""

# @app.route('/ok3')
# def get_pix_slip():
#     result = payment_controllers.create_pix_slip_payment()
#     return "sin"

# @app.route("/hook_pix")
# def hook_pix():
#     response = hook_controllers.create_hook_pix()
#     return "hook_pix"

# @app.route("/hook_pix_slip")
# def hook_pix_slip():
#     response = hook_controllers.create_hook_pix_slip()
#     return "hook_pix_slip"

# app.run(port=5000, host='localhost', debug=True)
