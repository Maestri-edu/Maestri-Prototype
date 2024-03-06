from dataclasses import dataclass
from enum import Enum


class CourseArea(Enum):
    legal_sciences = 1
    education = 2
    engineering_and_architecture = 3
    management_and_business = 4
    marketing_and_communication = 5
    health_and_wellness = 6
    information_technology = 7


class CourseDuration(Enum):
    eighteen_months = 1
    twenty_four_months = 2
    thirty_months = 3


class CourseGroup(Enum):
    G1 = 1
    G2 = 2
    G3 = 3
    G4 = 4
    R2 = 5


class CourseModality(Enum):
    face_to_face = 1
    education_at_a_distance = 2
    hybrid = 3


class CourseType(Enum):
    technologist = 1
    bachelors = 2
    licentiate = 3


@dataclass(order=True)
class Course:
    id: int
    name: str
    description: str
    information: str
    objective: str
    jobmarket: str
    specifics: str
    course_area_id: CourseArea
    course_duration_id: CourseDuration
    course_group_id: CourseGroup
    course_modality_id: CourseModality
    course_type_id: CourseType
