from typing import Optional
from common.contracts.pix_slip.pix_slip_payment_response import (
    PixSlipPaymentResponse,
    PaymentStatus,
    PaymentStatusDict,
)
from persistence.repositories import (
    ChargeRepository,
    EnrollmentRepository,
    ClientRepository,
)
from models.db_models.charge import Charge, ChargeSituation
from models.db_models.enrollment import Enrollment, EnrollmentStatus
from models.db_models.client import Client, ClientStatus, ClientType
from result import Err


class PixSlipProcessResponse:
    _charge_repository: ChargeRepository
    _enrollment_repository: EnrollmentRepository
    _client_repository: ClientRepository

    def __init__(
        self,
        charge_repository: ChargeRepository,
        enrollment_repository: EnrollmentRepository,
        client_repository: ClientRepository,
    ):
        self._charge_repository = charge_repository
        self._enrollment_repository = enrollment_repository
        self._client_repository = client_repository

    def process(self, payment_model: PixSlipPaymentResponse):

        if payment_model.status != PaymentStatus.payed.value:
            self._update_charge(payment_model)
            return

        # Get Charge -> Update Charge - OK

        charge: Optional[Charge] = self._charge_repository.select_by_solicitation_code(
            payment_model.solicitation_code
        )

        if charge is None:
            return

        charge.situation_id = ChargeSituation.recebido

        self._charge_repository.update(charge=charge)

        # Update Enrollment - Ok

        enrollment = self._enrollment_repository.select_by_id(
            charge.extract_id(charge.enrollment)
        )

        if enrollment is None:
            return

        enrollment.status_id = EnrollmentStatus.pending_awaiting_documentation

        self._enrollment_repository.update(enrollment)

        # Get Client -> Update Client from Lead to STudent - Ok

        client = self._client_repository.select_by_id(
            enrollment.extract_id(enrollment.client)
        )

        if client is None:
            return Err("Client Not Found")

        client.type_id = ClientType.student
        client.status_id = ClientStatus.data_pending

        self._client_repository.update(client=client)

        # Send Confirmation

        return

    def _update_charge(self, payment_model: PixSlipPaymentResponse):

        charge: Optional[Charge] = self._charge_repository.select_by_solicitation_code(
            payment_model.solicitation_code
        )

        if charge is None:
            return

        charge.situation_id = PaymentStatusDict.convert_to_charge_situation(
            payment_model.status
        )

        self._charge_repository.update(charge=charge)
