from typing import Optional, Union
from models.db_models.enrollment import Enrollment
from persistence.mother_base import MainDb


class EnrollmentRepository:

    def insert(self, enrollment: Enrollment):

        course_id = enrollment.extract_id(enrollment.course)
        client_id = enrollment.extract_id(enrollment.client)

        command = """INSERT INTO public.enrollment(number_of_installments, client_id, course_id, status_id) VALUES (%s, %s, %s, %s);"""

        values = (
            enrollment.number_of_installments,
            client_id,
            course_id,
            enrollment.status_id.value,
        )

        MainDb.run_command(command=command, values=values)

    def update(self, enrollment: Enrollment):

        client_id = enrollment.extract_id(enrollment.client)
        course_id = enrollment.extract_id(enrollment.course)

        command = """UPDATE public.enrollment SET number_of_installments=%s, client_id=%s, course_id=%s, status_id=%s WHERE id = %s;"""

        values = (
            enrollment.number_of_installments,
            client_id,
            course_id,
            enrollment.status_id.value,
            enrollment.id,
        )

        MainDb.run_command(command=command, values=values)

    def select_by_id(self, enrollment_id: int) -> Optional[Enrollment]:

        command = """SELECT id, number_of_installments, client_id, course_id, status_id FROM public.enrollment WHERE id = 1;"""
        values = (enrollment_id,)

        row = MainDb.run_query_single(command=command, values=values)

        if row is None:
            return None

        enrollment = Enrollment(
            id=row[0],
            number_of_installments=row[1],
            client=row[2],
            course=row[3],
            status_id=row[4],
        )

        return enrollment

    def select_all(self) -> list[Enrollment]:

        enrollments: list[Enrollment] = []

        command = """SELECT id, number_of_installments, client_id, course_id, status_id FROM public.enrollment"""

        result = MainDb.run_query(command=command, values=None)

        for row in result:
            enrollments.append(
                Enrollment(
                    id=row[0],
                    number_of_installments=row[1],
                    client=row[2],
                    course=row[3],
                    status_id=row[4],
                )
            )

        return enrollments

    def select_id_by_client_id(self, user_id: int) -> Optional[int]:

        command = """SELECT id FROM public.enrollment WHERE client_id = %s;"""
        values = (user_id,)

        row = MainDb.run_query_single(command=command, values=values)

        if row is None:
            return None

        return row[0]
