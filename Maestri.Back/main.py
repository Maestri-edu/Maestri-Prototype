from persistence.repositories.charge_repository import ChargeRepository, Charge
from persistence.repositories.client_repository import ClientRepository, Client
from persistence.repositories.course_repository import CourseRepository, Course
from persistence.repositories.enrollment_repository import EnrollmentRepository
from models.db_models.enrollment import Enrollment
from persistence.repositories.user_repository import UserRepository, User
from common.helper.datetime_provider import DatetimeProvider as dt
from models.db_models.user import UserType, UserStatus

from persistence.repositories import PersonalDataRepository
from models.db_models.personal_data import PersonalData, MaritalStatus, Gender

from apps.db.enrollment.complete_enrollment import (
    CompleteEnrollmentCommand,
    CompleteEnrollmentHandler,
)
from models.pix_slip.pix_slip_model import PixSlipModel
import json


def test_user_repository():

    _user_repository = UserRepository()

    # users = _user_repository.select_all()

    # for user in users:
    #     print(user)

    # user = User(
    #     id=0,
    #     username="username",
    #     password="New-superSecretPassword",
    #     creation_date=dt.now(),
    #     personal_data=None,
    #     status_id=UserStatus.active,
    #     type_id=UserType.user,
    # )

    # _user_repository.insert(user)

    # user = _user_repository.select_by_id(1)

    # if user is None:
    #     return 0

    # user.password = "supersenhanova"

    # _user_repository.update(user)

    # userd = _user_repository.select_by_id(1)

    # print("New User ", userd)


# def test_charge_repository():
#     _charge_repository = ChargeRepository()

#     charge = Charge(id=0,)


# def test_enrollment():
#     _enrollment_repository = EnrollmentRepository()

#     enrollment = Enrollment(id=0, number_of_installments=1, client=1, )


def test_course():

    _course_repo = CourseRepository()

    # courses = _course_repo.select_all()

    # for course in courses:
    #     print(course)

    course = _course_repo.select_by_id(63)

    if course is None:
        return

    print(course)
    print(course.course_type_id.name)


def test_personal_data():

    da = PersonalDataRepository()

    # model = PersonalData(
    #     id=0,
    #     name="SuperNomeLegal",
    #     rg="rgrgrg",
    #     cpf="cpfcpfcpf",
    #     phone="phonephone",
    #     birthdate=dt.now(),
    #     birthcity="birthCity",
    #     birthstate="PR",
    #     mother_name="Joana Majoria",
    #     email="emailemail",
    #     marital_status_id=MaritalStatus.divorced,
    #     gender_id=Gender.male,
    #     address=None,
    #     document=None,
    #     educational_data=None,
    # )

    # da.insert(model)

    # datas = da.select_all()

    # for data in datas:
    #     print(data)

    data = da.select_by_id(1)

    if data is None:
        return

    print(data)

    data.email = "Um novo email super top"
    da.update(data)

    print("\n\n\n\n", data)


def test_create_enrollment():
    CompleteEnrollmentHandler(EnrollmentRepository()).complete(
        CompleteEnrollmentCommand(id=0, number_of_installments=1, client=1, course=1)
    )


def test_pix_slip_model():
    data = """{ "cobranca": { "codigoSolicitacao": "183e982a-34e5-4bc0-9643-def5432a", "seuNumero": "12345678", "dataEmissao": "2023-09-24", "dataVencimento": "2023-10-15", "valorNominal": 1234.56, "tipoCobranca": "SIMPLES", "situacao": "RECEBIDO", "dataSituacao": "2023-09-26", "valorTotalRecebido": "1234.56", "origemRecebimento": "BOLETO", "arquivada": true, "descontos": [ { "codigo": "PERCENTUALDATAINFORMADA", "quantidadeDias": 7, "taxa": 5 } ], "multa": { "codigo": "VALORFIXO", "valor": 4 }, "mora": { "codigo": "TAXAMENSAL", "taxa": 5 }, "pagador": { "email": "nome.sobrenome@x.com.br", "ddd": "31", "telefone": "9999-9999", "numero": "3456", "complemento": "apartamento 3 bloco 4", "cpfCnpj": "12345678901", "tipoPessoa": "FISICA", "nome": "Nome do pagador", "endereco": "Avenida Brasil", "bairro": "Centro", "cidade": "Belo Horizonte", "uf": "MG", "cep": "30110000" } }, "boleto": { "nossoNumero": "12345678", "codigoBarras": "01234567890123456789012345678901234567890123", "linhaDigitavel": "01234567890123456789012345678901234567890123456" }, "pix": { "txid": "012345678901234567890123456789012345", "pixCopiaECola": "012345678901234567890BR.GOV.BCB.PIX2576spi-qrcode-h.bancointer.com.br..." } }"""
    json_data: dict = json.loads(data)["cobranca"]
    json_data.update(json.loads(data)["boleto"])
    json_data.update(json.loads(data)["pix"])

    pix_slip = PixSlipModel.create(json_data)

    print(pix_slip)


def check_unique():
    repo = PersonalDataRepository()

    result = repo.check_unique_constraint(
        cpf="10098212812", email="emailemail2@mailiantor.com"
    )

    print(result)


def main():
    # test_user_repository()
    # test_charge_repository()
    # test_client()
    # test_course()
    # test_personal_data()
    # test_create_enrollment()
    # test_pix_slip_model()
    check_unique()


if __name__ == "__main__":
    main()

# course_repository = CourseRepository()

# courses = course_repository.select_all()

# for course in courses:
#     print(course)

# import os
# import sys
# from persistence.repositories.user_repository import UserRepository
# from models.db_models.user import User, UserStatus, UserType
# from common.helper.datetime_provider import DatetimeProvider

# user_repository = UserRepository()

# user = user_repository.select_by_id(user_id=1)

# print(user)

# user = User(
#     id=0,
#     username="Paulo-Username",
#     password="superSenha",
#     creation_date=DatetimeProvider.now(),
#     status_id=UserStatus.active,
#     type_id=UserType.user,
#     personal_data=None,
# )

# user_repository.create(user)

# from services.token.auth import Auth
# from services.common.default_request import DefaultRequest
# from common.secrets.auth import AuthToken

# dr = DefaultRequest()
# at = Auth(dr)

# token = at.get_auth_token()

# print(token)

# # at._save_new_token("690812e1-a0cc-4919-a514-325ef8c0c97d")
# authToken = AuthToken()

# token = authToken.get_current_auth_token()

# print(token)

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
