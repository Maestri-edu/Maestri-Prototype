from typing import Optional, Union
from models.db_models.personal_data import (
    PersonalData,
    Address,
    Document,
    EducationalData,
    GraduationEducation,
    HighSchoolEducation,
    PostGraduationEducation,
)
from persistence.mother_base import MainDb
from models.db_models.personal_data import (
    SchoolingStatus,
    SchoolingType,
    SchoolType,
    Gender,
    MaritalStatus,
)


class PersonalDataRepository:

    def insert(self, personal_data: PersonalData):

        command = """INSERT INTO public.personal_data(name, rg, cpf, phone, birthdate, birthcity, birthstate, mothername, email, marital_status_id, 
        gender_id, address_id, document_id, educational_data_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        values = (
            personal_data.name,
            personal_data.rg,
            personal_data.cpf,
            personal_data.phone,
            personal_data.birthdate,
            personal_data.birthcity,
            personal_data.birthstate,
            personal_data.mother_name,
            personal_data.email,
            personal_data.marital_status_id.value,
            personal_data.gender_id.value,
            self.extract_id(personal_data.address),
            self.extract_id(personal_data.document),
            self.extract_id(personal_data.educational_data),
        )

        MainDb.run_command(command=command, values=values)

    def update(self, personal_data: PersonalData):

        command = """UPDATE public.personal_data SET name=%s, rg=%s, cpf=%s, phone=%s, birthdate=%s, birthcity=%s, birthstate=%s, mothername=%s, email=%s, marital_status_id=%s, gender_id=%s, address_id=%s, document_id=%s, educational_data_id=%s WHERE public.personal_data.id = %s;"""

        values = (
            personal_data.name,
            personal_data.rg,
            personal_data.cpf,
            personal_data.phone,
            personal_data.birthdate,
            personal_data.birthcity,
            personal_data.birthstate,
            personal_data.mother_name,
            personal_data.email,
            personal_data.marital_status_id.value,
            personal_data.gender_id.value,
            self.extract_id(personal_data.address),
            self.extract_id(personal_data.document),
            self.extract_id(personal_data.educational_data),
            personal_data.id,
        )

        MainDb.run_command(command=command, values=values)

    def select_all(self) -> list[PersonalData]:

        personal_data: list[PersonalData] = []

        command = """SELECT id, name, rg, cpf, phone, birthdate, birthcity, birthstate, mothername, email, marital_status_id, gender_id, address_id, document_id, educational_data_id FROM public.personal_data;"""

        result = MainDb.run_query(command, None)

        for row in result:
            personal_data.append(
                PersonalData(
                    id=row[0],
                    name=row[1],
                    rg=row[2],
                    cpf=row[3],
                    phone=row[4],
                    birthdate=row[5],
                    birthcity=row[6],
                    birthstate=row[7],
                    mother_name=row[8],
                    email=row[9],
                    marital_status_id=MaritalStatus(row[10]),
                    gender_id=Gender(row[11]),
                    address=row[12],
                    document=row[13],
                    educational_data=row[14],
                )
            )

        return personal_data

    def select_by_id(self, personal_data_id: int) -> Optional[PersonalData]:

        command = """SELECT name, rg, cpf, phone, birthdate, birthcity, birthstate, mothername, email, marital_status_id, gender_id, address_id, document_id, educational_data_id FROM public.personal_data WHERE id = %s;"""

        value = (personal_data_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        user = PersonalData(
            id=personal_data_id,
            name=row[0],
            rg=row[1],
            cpf=row[2],
            phone=row[3],
            birthdate=row[4],
            birthcity=row[5],
            birthstate=row[6],
            mother_name=row[7],
            email=row[8],
            marital_status_id=MaritalStatus(row[9]),
            gender_id=Gender(row[10]),
            address=row[11],
            document=row[12],
            educational_data=row[13],
        )

        return user

    def select_by_id_address(self, address_id: int) -> Optional[Address]:

        command = """SELECT id, postal_code, street, "number", neighborhood, additional_info, city, state, country FROM public.personal_data_address WHERE id = %s;"""

        value = (address_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        return Address(
            id=row[0],
            postal_code=row[1],
            street=row[2],
            number=row[3],
            neighborhood=row[4],
            additional_address_details=row[5],
            city=row[6],
            state=row[7],
            country=row[8],
        )

    def select_by_id_document(self, document_id: int) -> Optional[Document]:

        command = """SELECT id, profile_photo_url, identification_document_url, contract_url, signature_url, highschool_diploma_url, highschool_transcript_url, highschool_other_documents_url, graduation_diploma_url, graduation_transcript_url, graduation_other_documents_url, post_graduation_diploma_url, post_graduation_transcript_url, post_graduation_other_documents_url FROM public.personal_data_document WHERE id = %s;"""

        value = (document_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        return Document(
            id=row[0],
            profile_photo_url=row[1],
            identification_document_url=row[2],
            contract_url=row[3],
            signature_url=row[4],
            highschool_diploma_url=row[5],
            highschool_transcript_url=row[6],
            highschool_other_documents_url=row[7],
            graduation_diploma_url=row[8],
            graduation_transcript_url=row[9],
            graduation_other_documents_url=row[10],
            post_graduation_diploma_url=row[11],
            post_graduation_transcript_url=row[12],
            post_graduation_other_documents_url=row[13],
        )

    def select_by_id_educational_data(
        self, educational_data_id: int
    ) -> Optional[EducationalData]:

        command = """SELECT id, highschool_education_id, graduation_education_id, post_graduation_education_id FROM public.personal_data_educational_data WHERE id = %s;"""

        value = (educational_data_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        return EducationalData(
            id=row[0],
            highschool_education_id=row[1],
            graduation_education_id=row[2],
            post_graduation_education_id=row[3],
        )

    def select_by_id_graduation_education(
        self, graduation_education_id: int
    ) -> Optional[GraduationEducation]:

        command = """SELECT id, schooling_status_id, school_type_id, schooling_type_id, start_year, course_name, institution_name, city, state, completion_year, course_modality_id FROM public.personal_data_educational_data_graduation_education WHERE id = %s;"""

        value = (graduation_education_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        return GraduationEducation(
            id=row[0],
            schooling_status_id=SchoolingStatus(row),
            school_type_id=SchoolType(row),
            schooling_type_id=SchoolingType(row),
            start_year=row[4],
            course_name=row[5],
            institution_name=row[6],
            city=row[7],
            state=row[8],
            completion_year=row[9],
            course_modality_id=row[10],
        )

    def select_by_id_highschool_education(
        self, highschool_education_id: int
    ) -> Optional[HighSchoolEducation]:

        command = """SELECT id, schooling_status_id, school_type_id, schooling_type_id, start_year, institution_name, city, state, completion_year FROM public.personal_data_educational_data_highschool_education WHERE id = %s;"""

        value = (highschool_education_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        return HighSchoolEducation(
            id=row[0],
            schooling_status_id=SchoolingStatus(row),
            school_type_id=SchoolType(row),
            schooling_type_id=SchoolingType(row),
            institution_name=row[4],
            city=row[5],
            state=row[6],
            completion_year=row[7],
        )

    def select_by_id_post_graduation_education(
        self, post_graduation_education_id: int
    ) -> Optional[PostGraduationEducation]:

        command = """SELECT id, schooling_status_id, school_type_id, schooling_type_id, institution_name, city, state, completion_year FROM public.personal_data_educational_data_highschool_education WHERE id = %s;"""

        value = (post_graduation_education_id,)

        row = MainDb.run_query_single(command, value)

        if row is None:
            return None

        return PostGraduationEducation(
            id=row[0],
            schooling_status_id=SchoolingStatus(row),
            school_type_id=SchoolType(row),
            schooling_type_id=SchoolingType(row),
            course_type=row[4],
            start_year=row[5],
            course_name=row[6],
            institution_name=row[7],
            city=row[8],
            state=row[9],
            completion_year=row[10],
            course_modality_id=row[11],
        )

    def select_id_by_email(self, email: str):
        command = """SELECT id FROM public.personal_data WHERE email = %s;"""
        value = (email,)
        row = MainDb.run_query_single(command, value)
        if row is None:
            return None
        return row[0]

    def check_unique_constraint(self, cpf: str, email: str) -> list[bool]:

        cpf_row = MainDb.run_query_single(
            command="""SELECT id from public.personal_data where cpf = %s;""",
            values=(cpf,),
        )

        email_row = MainDb.run_query_single(
            command=""" SELECT id from public.personal_data where email = %s""",
            values=(email,),
        )

        return [cpf_row is not None, email_row is not None]

    def extract_id(
        self, model: Union[Address, Document, EducationalData, int, None]
    ) -> Optional[int]:

        if isinstance(model, int):
            return model
        elif model is None:
            return None
        else:
            return model.id
