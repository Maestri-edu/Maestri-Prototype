from persistence.repositories.enrollment_repository import EnrollmentRepository
from models.db_models.enrollment import Enrollment, EnrollmentStatus
from dataclasses import dataclass


# Insert:
# Primeiro, criamos um objeto do tipo Enrollment, que é uma classe de dados que representa uma matrícula.
# Para isso devemos passar os parâmetros necessários para a criação do objeto.
# Iremos utilizar o método insert do EnrollmentRepository para inserir a matrícula no banco de dados.


@dataclass
class CompleteEnrollmentCommand:
    id: int
    number_of_installments: int
    client: int
    course: int


class CompleteEnrollmentHandler:
    _enrollment_repository: EnrollmentRepository

    def __init__(self, enrollment_repository: EnrollmentRepository):
        self._enrollment_repository = enrollment_repository

    def complete(self, command: CompleteEnrollmentCommand):
        self._enrollment_repository.insert(
            Enrollment(
                id=command.id,
                number_of_installments=command.number_of_installments,
                client=command.client,
                course=command.course,
                status_id=EnrollmentStatus.pending_awaiting_registration_fee_payment,
            )
        )
