from dataclasses import dataclass
from models.db_models.course import Course


@dataclass
class UpdateCourseCommand:
    course_id: int
