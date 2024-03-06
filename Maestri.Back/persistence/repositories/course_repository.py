from typing import Optional
from persistence.mother_base import MainDb
from models.db_models.course import (
    Course,
    CourseArea,
    CourseDuration,
    CourseGroup,
    CourseModality,
    CourseType,
)


class CourseRepository:

    def insert(self, course: Course):

        command = """INSERT INTO public.course(course_name, description, information, objective, jobmarket, specifics, course_area_id, course_duration_id, course_group_id, course_modality_id, course_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        values = (
            course.name,
            course.description,
            course.information,
            course.objective,
            course.jobmarket,
            course.specifics,
            course.course_area_id.value,
            course.course_duration_id.value,
            course.course_group_id.value,
            course.course_modality_id.value,
            course.course_type_id.value,
        )

        MainDb.run_command(command=command, values=values)

    def update(self, course: Course):

        command = """UPDATE public.course SET id=%s, course_name=%s, description=%s, information=%s, objective=%s, jobmarket=%s, specifics=%s, course_area_id=%s, course_duration_id=%s, course_group_id=%s, course_modality_id=%s, course_type_id=%s WHERE id = %s;"""

        values = (
            course.id,
            course.name,
            course.description,
            course.information,
            course.objective,
            course.jobmarket,
            course.specifics,
            course.course_area_id.value,
            course.course_duration_id.value,
            course.course_group_id.value,
            course.course_modality_id.value,
            course.course_type_id.value,
        )

        MainDb.run_command(command=command, values=values)

    def select_by_id(self, id: int) -> Optional[Course]:

        command = """SELECT id, course_name, description, information, objective, jobmarket, specifics, 
        course_area_id, course_duration_id, course_group_id, course_modality_id, course_type_id FROM public.course WHERE ID = %s;"""

        row = MainDb.run_query_single(command, (id,))

        if row is None:
            return None

        course = Course(
            id=row[0],
            name=row[1],
            description=row[2],
            information=row[3],
            objective=row[4],
            jobmarket=row[5],
            specifics=row[6],
            course_area_id=CourseArea(row[7]),
            course_duration_id=CourseDuration(row[8]),
            course_group_id=CourseGroup(row[9]),
            course_modality_id=CourseModality(row[10]),
            course_type_id=CourseType(row[11]),
        )

        return course

    def select_all(self) -> list[Course]:

        courses: list[Course] = []

        command = """SELECT id, course_name, description, information, objective, jobmarket, specifics, 
        course_area_id, course_duration_id, course_group_id, course_modality_id, course_type_id FROM public.course;"""

        result = MainDb.run_query(command, None)

        for row in result:
            courses.append(
                Course(
                    id=row[0],
                    name=row[1],
                    description=row[2],
                    information=row[3],
                    objective=row[4],
                    jobmarket=row[5],
                    specifics=row[6],
                    course_area_id=CourseArea(row[7]),
                    course_duration_id=CourseDuration(row[8]),
                    course_group_id=CourseGroup(row[9]),
                    course_modality_id=CourseModality(row[10]),
                    course_type_id=CourseType(row[11]),
                )
            )

        return courses
