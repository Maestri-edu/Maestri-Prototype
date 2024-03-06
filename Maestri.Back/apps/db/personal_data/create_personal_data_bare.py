from dataclasses import dataclass
from models.db_models.personal_data import (
    PersonalData,
    MaritalStatus,
    Gender,
)
from datetime import date
from persistence.repositories import PersonalDataRepository


@dataclass
class CreatePersonalDataBareCommand:
    name: str
    cpf: str
    phone: str
    email: str


class CreatePersonalDataBareHandler:
    _personal_data_repository: PersonalDataRepository

    def __init__(self, personal_data_repository: PersonalDataRepository):
        self._personal_data_repository = personal_data_repository

    def create(self, command: CreatePersonalDataBareCommand):

        data = PersonalData(
            id=0,
            name=command.name,
            rg="",
            cpf=command.cpf,
            phone=command.phone,
            birthdate=date.min,
            birthcity="",
            birthstate="",
            mother_name="",
            email=command.email,
            marital_status_id=MaritalStatus.single,
            gender_id=Gender.male,
            address=None,
            document=None,
            educational_data=None,
        )

        self._personal_data_repository.insert(data)
