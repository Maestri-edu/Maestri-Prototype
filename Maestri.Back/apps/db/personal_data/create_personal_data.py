from dataclasses import dataclass
from models.db_models.personal_data import (
    PersonalData,
    MaritalStatus,
    Gender,
)
from datetime import date
from persistence.repositories import PersonalDataRepository


@dataclass
class CreatePersonalDataCommand:
    name: str
    rg: str
    cpf: str
    phone: str
    birthdate: date
    birthcity: str
    birthstate: str
    mother_name: str
    email: str
    marital_status_id: MaritalStatus
    gender_id: Gender


class CreatePersonalDataHandler:
    _personal_data_repository: PersonalDataRepository

    def __init__(self, personal_data_repository: PersonalDataRepository):
        self._personal_data_repository = personal_data_repository

    def create(self, command: CreatePersonalDataCommand):

        data = PersonalData(
            id=0,
            name=command.name,
            rg=command.rg,
            cpf=command.cpf,
            phone=command.phone,
            birthdate=command.birthdate,
            birthcity=command.birthcity,
            birthstate=command.birthstate,
            mother_name=command.mother_name,
            email=command.email,
            marital_status_id=command.marital_status_id,
            gender_id=command.gender_id,
            address=None,
            document=None,
            educational_data=None,
        )

        self._personal_data_repository.insert(data)
