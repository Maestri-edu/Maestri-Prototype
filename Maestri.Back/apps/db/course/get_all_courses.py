from persistence.repositories import CourseRepository
from models.db_models.course import Course


class GetAllCourses:

    _course_repository: CourseRepository

    def __init__(self, course_repository: CourseRepository):
        self._course_repository = course_repository

    def get_all(self) -> list[Course]:

        return self._course_repository.select_all()
