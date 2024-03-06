from typing import Optional
import psycopg2
from common.secrets.db_config import MainDbConfig as db


class MainDb:
    @staticmethod
    def create_connection():
        return psycopg2.connect(
            database=db.DATABASE_NAME,
            host=db.HOST,
            user=db.USER,
            password=db.PASSWORD,
            port=db.PORT,
        )

    @staticmethod
    def run_command(command: str, values: tuple):
        connection = MainDb.create_connection()

        cursor = connection.cursor()

        cursor.execute(command, values)

        connection.commit()

        connection.close()

    @staticmethod
    def run_query(command: str, values: Optional[tuple]) -> list[tuple]:

        connection = MainDb.create_connection()
        cursor = connection.cursor()

        if isinstance(values, tuple):
            cursor.execute(command, values)
        else:
            cursor.execute(command)

        return cursor.fetchall()

    @staticmethod
    def run_query_single(command: str, values: Optional[tuple]) -> Optional[tuple]:

        connection = MainDb.create_connection()
        cursor = connection.cursor()

        if isinstance(values, tuple):
            cursor.execute(command, values)
        else:
            cursor.execute(command)

        return cursor.fetchone()
