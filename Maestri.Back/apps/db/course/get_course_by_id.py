from typing import Optional
from persistence.repositories import CourseRepository
from models.db_models.course import Course
from dataclasses import dataclass


@dataclass
class GetCourseByIdQuery:
    course_id: int


class GetCourseById:
    _course_repository: CourseRepository

    def __init__(self, course_repository: CourseRepository) -> None:
        self._course_repository = course_repository

    def get_by_id(self, command: GetCourseByIdQuery) -> Optional[Course]:

        return self._course_repository.select_by_id(command.course_id)
