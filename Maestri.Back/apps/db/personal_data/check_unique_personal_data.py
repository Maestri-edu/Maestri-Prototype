from dataclasses import dataclass
from persistence.repositories import PersonalDataRepository
from services.common.default_request import ErrorResponse, SuccessResponse
from result import Err, Ok
from common.errors.personal_data import PersonalDataError


@dataclass(frozen=True, order=True)
class CheckUniquePersonalDataQuery:
    email: str
    cpf: str


class CheckUniquePersonalDataHandler:

    _personal_data_repository: PersonalDataRepository

    def __init__(self, personal_data_repository: PersonalDataRepository) -> None:
        self._personal_data_repository = personal_data_repository

    def check_unique(
        self, query: CheckUniquePersonalDataQuery
    ) -> Ok[str] | Err[ErrorResponse]:

        result = self._personal_data_repository.check_unique_constraint(
            cpf=query.cpf, email=query.email
        )

        if result[0] and result[1]:
            return Err(
                ErrorResponse(status_code=403, data={"data": "Email e CPF já em uso"})
            )

        if result[0]:
            return Err(PersonalDataError._duplicate_cpf)

        if result[1]:
            return Err(PersonalDataError._duplicate_email)

        return Ok("")
