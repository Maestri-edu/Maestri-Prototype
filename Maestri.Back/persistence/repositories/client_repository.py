from typing import Optional
from models.db_models.client import Client, PersonalData, User
from persistence.mother_base import MainDb


class ClientRepository:

    def insert(self, client: Client):

        personal_data_id = None

        if isinstance(client.personal_data, int):
            personal_data_id = client.personal_data
        elif isinstance(client.personal_data, PersonalData):
            personal_data_id = client.personal_data.id

        user_id = None

        if isinstance(client.user, User):
            user_id = client.user.id
        else:
            user_id = client.user

        command = """INSERT INTO public.client(registration_date, user_id, personal_data_id, status_id, type_id) VALUES (%s, %s, %s, %s, %s);"""

        values = (
            client.registration_date,
            user_id,
            personal_data_id,
            client.status_id.value,
            client.type_id.value,
        )

        MainDb.run_command(command=command, values=values)

    def update(self, client: Client):

        command = """UPDATE public.client SET status_id=%s, type_id=%s WHERE id = %s;"""

        values = (client.status_id.value, client.type_id.value, client.id)

        MainDb.run_command(command=command, values=values)

    def select_by_id(self, id: int) -> Optional[Client]:

        command = """SELECT id, registration_date, user_id, personal_data_id, status_id, type_id FROM public.client WHERE id = %s;"""

        values = (id,)

        row = MainDb.run_query_single(command=command, values=values)

        if row is None:
            return None

        client = Client(
            id=row[0],
            registration_date=row[1],
            user=row[2],
            personal_data=row[3],
            status_id=row[4],
            type_id=row[5],
        )

        return client

    def select_id_by_user_id(self, user_id: int) -> Optional[int]:
        command = """SELECT id FROM public.client WHERE user_id = %s;"""
        values = (user_id,)
        row = MainDb.run_query_single(command=command, values=values)
        if row is None:
            return None
        return row[0]
