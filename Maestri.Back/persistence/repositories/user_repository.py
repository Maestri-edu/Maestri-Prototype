from typing import Optional
from models.db_models.user import User, UserStatus, UserType
from models.db_models.personal_data import PersonalData, MaritalStatus, Gender
from persistence.mother_base import MainDb


class UserRepository:

    def insert(self, user: User):

        command = """INSERT INTO public."user"(username, password, creation_date, status_id, type_id, personal_data_id) VALUES (%s, %s, %s, %s, %s, %s);"""

        values = (
            user.username,
            user.password,
            user.creation_date,
            user.status_id.value,
            user.type_id.value,
            user.extract_id(user.personal_data),
        )

        MainDb.run_command(command=command, values=values)

    def update(self, user: User):

        command = """UPDATE public."user" SET username=%s, password=%s, status_id=%s, type_id=%s WHERE public."user".id=%s;"""

        values = (user.username, user.password, user.status_id, user.type_id, user.id)

        MainDb.run_command(command=command, values=values)

    def select_all(self) -> list[User]:

        users: list[User] = []

        command = """SELECT id, username, password, creation_date, status_id, type_id, personal_data_id FROM public."user";"""

        result = MainDb.run_query(command, None)

        for row in result:
            users.append(
                User(
                    id=row[0],
                    username=row[1],
                    password=row[2],
                    creation_date=row[3],
                    status_id=UserStatus(row[4]),
                    type_id=UserType(row[5]),
                    personal_data=row[6],
                )
            )

        return users

    def select_by_id(self, user_id: int) -> Optional[User]:

        command = """SELECT username, password, creation_date, status_id, type_id, personal_data_id FROM public."user" WHERE public.user.id = %s;"""

        value = (user_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        user = User(
            id=user_id,
            username=row[0],
            password=row[1],
            creation_date=row[2],
            status_id=UserStatus(row[4]),
            type_id=UserType(row[5]),
            personal_data=row[5],
        )

        return user

    def select_by_id_full(self, user_id: int) -> Optional[User]:

        command = """SELECT username, password, creation_date, status_id, type_id, pd.id, pd.name, pd.rg, pd.cpf, pd.phone, pd.birthdate, pd.birthcity, pd.birthstate, pd.mothername, email, pd.marital_status_id, pd.gender_id, pd.address_id, pd.document_id, pd.educational_data_id FROM public."user" as us JOIN public.personal_data as pd on us.personal_data_id = pd.id WHERE us.id = 1;"""

        value = (user_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        user = User(
            id=user_id,
            username=row[0],
            password=row[1],
            creation_date=row[2],
            status_id=UserStatus(row[3]),
            type_id=UserType(row[4]),
            personal_data=PersonalData(
                id=row[5],
                name=row[6],
                rg=row[7],
                cpf=row[8],
                phone=row[9],
                birthdate=row[10],
                birthcity=row[11],
                birthstate=row[12],
                mother_name=row[13],
                email=row[14],
                marital_status_id=MaritalStatus(row[15]),
                gender_id=Gender(row[16]),
                address=row[17],
                document=row[18],
                educational_data=row[19],
            ),
        )

        return user

    def select_by_username(self, username: str) -> Optional[User]:

        command = """SELECT id, password, creation_date, status_id, type_id, personal_data_id FROM public."user" WHERE public.user.username = %s;"""

        value = (username,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        user = User(
            id=row[0],
            username=username,
            password=row[1],
            creation_date=row[2],
            status_id=UserStatus(row[3]),
            type_id=UserType(row[4]),
            personal_data=row[5],
        )

        return user
