import uuid
from common.contracts.campaign.create_pix_slip_payment import (
    CreateCampaignPixSlipPayment,
)
from common.enums.person_enums import PersonType, UF
from common.helper.datetime_provider import DatetimeProvider as dt
from models.common.payer_model import PayerModel, Address
from models.pix_slip.pix_slip_payment_model import PixSlipPaymentModel
from services.pix_slip.pix_slip_service import PixSlipService
from common.errors.campaign import PixSlipCampaignError
from apps.db.user.register_user import RegisterUser, RegisterUserCommand
from apps.db.personal_data.create_personal_data_bare import (
    CreatePersonalDataBareHandler,
    CreatePersonalDataBareCommand,
)
from result import Err, Ok
import datetime
from apps.db.client.register_client import RegisterClientHandler, RegisterClientCommand
from persistence.repositories import (
    ClientRepository,
    UserRepository,
    PersonalDataRepository,
)
from apps.db.enrollment.complete_enrollment import (
    CompleteEnrollmentCommand,
    CompleteEnrollmentHandler,
)
from persistence.repositories import EnrollmentRepository
from apps.db.charge.create_charge import CreateChargeCommand, CreateChargeHandler
from apps.db.personal_data.check_unique_personal_data import (
    CheckUniquePersonalDataQuery,
    CheckUniquePersonalDataHandler,
)
from services.pix_slip.pix_slip_service import PixSlipService
from models.pix_slip.pix_slip_model import PixSlipModel
from services.common.default_request import ErrorResponse, SuccessResponse
from django.contrib.auth.hashers import make_password
from secrets import choice
import string


class PixSlipPayment:
    _pix_slip: PixSlipService
    _register_user: RegisterUser
    _create_personal_data: CreatePersonalDataBareHandler
    _register_client: RegisterClientHandler
    _client_repository: ClientRepository
    _user_repository: UserRepository
    _personal_data_repository: PersonalDataRepository
    _complete_enrollment: CompleteEnrollmentHandler
    _enrollment_repository: EnrollmentRepository
    _create_charge: CreateChargeHandler
    _pix_slip_service: PixSlipService
    _check_personal_data: CheckUniquePersonalDataHandler

    def __init__(
        self,
        pix_slip: PixSlipService,
        register_user: RegisterUser,
        create_personal_data: CreatePersonalDataBareHandler,
        register_client: RegisterClientHandler,
        client_repository: ClientRepository,
        user_repository: UserRepository,
        personal_data_repository: PersonalDataRepository,
        complete_enrollment: CompleteEnrollmentHandler,
        enrollment_repository: EnrollmentRepository,
        create_charge: CreateChargeHandler,
        pix_slip_service: PixSlipService,
        check_personal_data: CheckUniquePersonalDataHandler,
    ):
        self._pix_slip = pix_slip
        self._register_user = register_user
        self._create_personal_data = create_personal_data
        self._register_client = register_client
        self._client_repository = client_repository
        self._user_repository = user_repository
        self._personal_data_repository = personal_data_repository
        self._complete_enrollment = complete_enrollment
        self._enrollment_repository = enrollment_repository
        self._create_charge = create_charge
        self._pix_slip_service = pix_slip_service
        self._check_personal_data = check_personal_data

    def create_payment(
        self, request: CreateCampaignPixSlipPayment
    ) -> Err[ErrorResponse] | Ok[SuccessResponse]:

        query = CheckUniquePersonalDataQuery(request.payer_email, request.payer_id)

        result = self._check_personal_data.check_unique(query)

        if isinstance(result, Err):
            return result

        if not CampaignPixSlipValidator.validate(request):
            return Err(PixSlipCampaignError.invalid_fields)

        payment_due_date = dt.utc_now() + datetime.timedelta(days=1)

        payment = PixSlipPaymentModel(
            title_number="80",
            value=request.payment_value,
            due_date=payment_due_date,
            due_date_spare_limit=7,
            payer=PayerModel(
                id_number=request.payer_id,
                name=request.payer_name,
                email=request.payer_email,
                type=PersonType.PF,
                telephone=request.payer_telephone,
                adress=Address(
                    cep_number=request.payer_cep,
                    complete_adress="Rua Doutor Argemiro Couto de Barros",
                    uf=UF.SP,
                    city="São Paulo",
                    neighborhood="Rodigues Almirante",
                    number="100",
                    complement="",
                ),
            ),
        )

        # payment = self._pix_slip.emit_payment(payment)

        # if isinstance(payment, Err):
        #     return payment

        personal_data_command = CreatePersonalDataBareCommand(
            name=request.payer_name,
            cpf=request.payer_id,
            phone=request.payer_telephone.get_complete_number(),
            email=request.payer_email,
        )

        self._create_personal_data.create(personal_data_command)

        personal_id = self._personal_data_repository.select_id_by_email(
            personal_data_command.email
        )

        user_command = RegisterUserCommand(
            username=request.payer_name,
            password=make_password(
                "".join(
                    [choice(string.ascii_uppercase + string.digits) for _ in range(10)]
                )
            ),
            personal_data=personal_id,
        )

        self._register_user.register(user_command)
        user_db = self._user_repository.select_by_username(user_command.username)

        if user_db is None:
            return Err(PixSlipCampaignError.user_not_found)

        client_command = RegisterClientCommand(
            user_id=user_db.id, personal_data_id=personal_id
        )

        self._register_client.register(client_command)
        client_id = self._client_repository.select_id_by_user_id(user_db.id)

        if client_id is None:
            return Err(PixSlipCampaignError.client_not_found)

        enrollment_command = CompleteEnrollmentCommand(
            id=0, number_of_installments=1, client=client_id, course=request.course_id
        )

        self._complete_enrollment.complete(enrollment_command)

        enrollment_id = self._enrollment_repository.select_id_by_client_id(client_id)

        if enrollment_id is None:
            return Err(PixSlipCampaignError.enrollment_not_found)

        # payment_solicitation_code = payment.ok_value.data["codigoSolicitacao"]
        payment_solicitation_code = str(uuid.uuid4())

        # response = self._pix_slip_service.get_payment_data(payment_solicitation_code)

        # if isinstance(response, Err):
        #     return Err(PixSlipCampaignError.not_found)

        # data = response.ok_value.data

        # json_data: dict = data["cobranca"]
        # json_data.update(data["boleto"])
        # json_data.update(data["pix"])

        # pix_slip = PixSlipModel.create(json_data)

        # charge_command = CreateChargeCommand(
        #     enrollment=enrollment_id,
        #     solicitation_code=payment_solicitation_code,
        #     your_number=pix_slip.account_number,
        #     our_number="",
        #     received_value=pix_slip.received_value,
        #     payment_origin=pix_slip.payment_origin,
        #     bar_code=pix_slip.bar_code,
        #     typed_code=pix_slip.typed_code,
        #     txid=pix_slip.txid,
        #     simple_pix_code=pix_slip.simple_pix_code,
        # )

        charge_command = CreateChargeCommand(
            enrollment=enrollment_id,
            solicitation_code=payment_solicitation_code,
            your_number="account",
            our_number="",
            received_value=request.payment_value,
            payment_origin="origin",
            bar_code="bar code",
            typed_code="typedcode",
            txid="txid",
            simple_pix_code="simple pix code",
        )

        self._create_charge.create(charge_command)

        return Ok(
            SuccessResponse(
                status_code=200,
                data={
                    "solicitation_code": payment_solicitation_code,
                    "data": payment.json_request_body(),
                },
            )
        )


class CampaignPixSlipValidator:
    @staticmethod
    def validate(model: CreateCampaignPixSlipPayment) -> bool:

        if model.payment_value < 1300 or model.payment_value > 1600:
            return False

        return True
