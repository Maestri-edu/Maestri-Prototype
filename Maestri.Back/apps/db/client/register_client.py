from dataclasses import dataclass
from typing import Union
from models.db_models.client import Client, ClientStatus, ClientType
from persistence.repositories import ClientRepository
from common.helper.datetime_provider import DatetimeProvider as dt


@dataclass
class RegisterClientCommand:
    user_id: int
    personal_data_id: Union[int, None]


class RegisterClientHandler:

    _client_repository: ClientRepository

    def __init__(self, client_repository: ClientRepository) -> None:
        self._client_repository = client_repository

    def register(self, command: RegisterClientCommand):

        client = Client(
            id=0,
            registration_date=dt.now(),
            user=command.user_id,
            personal_data=command.personal_data_id,
            status_id=ClientStatus.financial_pending,
            type_id=ClientType.lead,
        )

        self._client_repository.insert(client)
