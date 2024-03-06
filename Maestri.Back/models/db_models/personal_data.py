from dataclasses import dataclass
from enum import Enum
from datetime import date
from typing import Optional, Union


class MaritalStatus(Enum):
    single = 1
    married = 2
    divorced = 3
    widower = 4


class Gender(Enum):
    male = 1
    female = 2


class SchoolingStatus(Enum):
    conlcluded = 1
    in_progress = 2
    not_started = 3


class SchoolType(Enum):
    face_to_face = 1
    education_at_a_distance = 2
    hybrid = 3


class SchoolingType(Enum):
    public = 1
    private = 2


@dataclass(order=True)
class PostGraduationEducation:
    id: int
    schooling_status_id: SchoolingStatus
    school_type_id: SchoolType
    schooling_type_id: SchoolingType
    course_type: int
    start_year: int
    course_name: str
    institution_name: str
    city: str
    state: str
    completion_year: int
    course_modality_id: int


@dataclass(order=True)
class GraduationEducation:
    id: int
    schooling_status_id: SchoolingStatus
    school_type_id: SchoolType
    schooling_type_id: SchoolingType
    start_year: int
    course_name: str
    institution_name: str
    city: str
    state: str
    completion_year: int
    course_modality_id: int


@dataclass(order=True)
class HighSchoolEducation:
    id: int
    schooling_status_id: SchoolingStatus
    school_type_id: SchoolType
    schooling_type_id: SchoolingType
    institution_name: str
    city: str
    state: str
    completion_year: int


@dataclass(order=True)
class EducationalData:
    id: int
    highschool_education_id: Optional[HighSchoolEducation]
    graduation_education_id: Optional[GraduationEducation]
    post_graduation_education_id: Optional[PostGraduationEducation]


@dataclass(order=True)
class Address:
    id: int
    postal_code: str
    street: str
    number: str
    neighborhood: str
    additional_address_details: str
    city: str
    state: str
    country: str


@dataclass(order=True)
class Document:
    id: int
    profile_photo_url: str
    identification_document_url: str
    contract_url: str
    signature_url: str
    highschool_diploma_url: str
    highschool_transcript_url: str
    highschool_other_documents_url: str
    graduation_diploma_url: str
    graduation_transcript_url: str
    graduation_other_documents_url: str
    post_graduation_diploma_url: str
    post_graduation_transcript_url: str
    post_graduation_other_documents_url: str


@dataclass(order=True)
class PersonalData:
    id: int
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
    address: Union[Address, int, None]
    document: Union[Document, int, None]
    educational_data: Union[EducationalData, int, None]

    def extract_id(self, value: Union[Address, Document, EducationalData]) -> int:

        if isinstance(value, int):
            return value

        return value.id
