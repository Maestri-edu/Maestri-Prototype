from typing import Optional
from uuid import UUID
from persistence.mother_base import MainDb
from models.db_models.charge import Charge


class ChargeRepository:

    def insert(self, charge: Charge):

        command = """INSERT INTO public.charge(enrollment_id, type_id, situation_id, solicitation_code, your_number, our_number,
          received_datetime, received_value, payment_origin, bar_code, typed_code, txid, simple_pix_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

        values = (
            charge.extract_id(charge.enrollment),
            charge.type_id.value,
            charge.situation_id.value,
            charge.solicitation_code,
            charge.your_number,
            charge.our_number,
            charge.received_datetime,
            charge.received_value,
            charge.payment_origin,
            charge.bar_code,
            charge.typed_code,
            charge.txid,
            charge.simple_pix_code,
        )

        MainDb.run_command(command=command, values=values)

    def update(self, charge: Charge):

        command = """UPDATE public.charge SET enrollment_id=%s, type_id=%s, situation_id=%s, solicitation_code=%s, your_number=%s, our_number=%s, received_datetime=%s, received_value=%s, payment_origin=%s, bar_code=%s, typed_code=%s, txid=%s, simple_pix_code=%s WHERE id = %s;"""

        values = (
            charge.extract_id(charge.enrollment),
            charge.type_id,
            charge.situation_id,
            charge.solicitation_code,
            charge.your_number,
            charge.our_number,
            charge.received_datetime,
            charge.received_value,
            charge.payment_origin,
            charge.bar_code,
            charge.typed_code,
            charge.txid,
            charge.simple_pix_code,
            charge.id,
        )

        MainDb.run_command(command=command, values=values)

    def select_by_id(self, id: int) -> Optional[Charge]:

        command = """SELECT id, enrollment_id, type_id, situation_id, solicitation_code, your_number, our_number, received_datetime, received_value, payment_origin, bar_code, typed_code, txid, simple_pix_code FROM public.charge WHERE id = %s;"""

        values = (id,)

        row = MainDb.run_query_single(command=command, values=values)

        if row is None:
            return None

        charge = Charge(
            id=row[0],
            enrollment=row[1],
            type_id=row[2],
            situation_id=row[3],
            solicitation_code=row[4],
            your_number=row[5],
            our_number=row[6],
            received_datetime=row[7],
            received_value=row[8],
            payment_origin=row[9],
            bar_code=row[10],
            typed_code=row[11],
            txid=row[12],
            simple_pix_code=row[13],
        )

        return charge

    def select_by_txid(self, id: UUID) -> Optional[Charge]:

        command = """SELECT id, enrollment_id, type_id, situation_id, solicitation_code, your_number, our_number, received_datetime, received_value, payment_origin, bar_code, typed_code, txid, simple_pix_code FROM public.charge WHERE txid = %s;"""

        values = (str(id),)

        row = MainDb.run_query_single(command=command, values=values)

        if row is None:
            return None

        charge = Charge(
            id=row[0],
            enrollment=row[1],
            type_id=row[2],
            situation_id=row[3],
            solicitation_code=row[4],
            your_number=row[5],
            our_number=row[6],
            received_datetime=row[7],
            received_value=row[8],
            payment_origin=row[9],
            bar_code=row[10],
            typed_code=row[11],
            txid=row[12],
            simple_pix_code=row[13],
        )

        return charge

    def select_by_solicitation_code(self, solicitation_code: str) -> Optional[Charge]:

        command = """SELECT id, enrollment_id, type_id, situation_id, your_number, our_number, received_datetime, received_value, payment_origin, bar_code, typed_code, txid, simple_pix_code
	FROM public.charge; WHERE solicitation_code = %s;"""

        values = (solicitation_code,)

        row = MainDb.run_query_single(command=command, values=values)

        if row is None:
            return None

        charge = Charge(
            id=row[0],
            enrollment=row[1],
            type_id=row[2],
            situation_id=row[3],
            solicitation_code=row[4],
            your_number=row[5],
            our_number=row[6],
            received_datetime=row[7],
            received_value=row[8],
            payment_origin=row[9],
            bar_code=row[10],
            typed_code=row[11],
            txid=row[12],
            simple_pix_code=row[13],
        )

        return charge
