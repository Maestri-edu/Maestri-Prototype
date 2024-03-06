from common.factories.pix_slip_factory import PixSlipServiceFactory
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
from result import Err
import datetime
from models.db_models.charge import Charge, ChargeSituation, ChargeType
from models.db_models.enrollment import Enrollment, EnrollmentStatus
from models.db_models.client import Client, ClientStatus, ClientType
from apps.db.client.register_client import RegisterClientHandler, RegisterClientCommand
from persistence.repositories import (
    ClientRepository,
    UserRepository,
    PersonalDataRepository,
    ChargeRepository,
)
from apps.db.enrollment.complete_enrollment import (
    CompleteEnrollmentCommand,
    CompleteEnrollmentHandler,
)
from persistence.repositories import EnrollmentRepository
from apps.db.charge.create_charge import CreateChargeCommand, CreateChargeHandler
from services.pix_slip.pix_slip_service import PixSlipService
from models.pix_slip.pix_slip_model import PixSlipModel
from apps.campaign.pix_slip_payment import PixSlipPayment
from services.token.auth import Auth
from services.common.default_request import DefaultRequest
from apps.db.personal_data.check_unique_personal_data import (
    CheckUniquePersonalDataHandler,
)


class PixSlipPaymentFactory:

    @staticmethod
    def create():

        dr = DefaultRequest()
        auth = Auth(dr=dr)

        user_repository = UserRepository()
        personal_data = PersonalDataRepository()
        client = ClientRepository()
        enrollment_repository = EnrollmentRepository()
        charge_repository = ChargeRepository()

        return PixSlipPayment(
            pix_slip=PixSlipService(dr, auth),
            register_user=RegisterUser(user_repository),
            create_personal_data=CreatePersonalDataBareHandler(personal_data),
            register_client=RegisterClientHandler(client),
            client_repository=ClientRepository(),
            user_repository=UserRepository(),
            personal_data_repository=PersonalDataRepository(),
            complete_enrollment=CompleteEnrollmentHandler(enrollment_repository),
            enrollment_repository=EnrollmentRepository(),
            create_charge=CreateChargeHandler(charge_repository),
            pix_slip_service=PixSlipService(dr, auth),
            check_personal_data=CheckUniquePersonalDataHandler(
                personal_data_repository=personal_data
            ),
        )
