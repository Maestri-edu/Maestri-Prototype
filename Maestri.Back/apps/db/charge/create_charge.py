from persistence.repositories.charge_repository import ChargeRepository
from models.db_models.charge import ChargeType, ChargeSituation, Charge
from dataclasses import dataclass
from datetime import datetime
from common.helper.datetime_provider import DatetimeProvider as dt


@dataclass
class CreateChargeCommand:
    enrollment: int
    solicitation_code: str
    your_number: str
    our_number: str
    received_value: float
    payment_origin: str
    bar_code: str
    typed_code: str
    txid: str
    simple_pix_code: str


class CreateChargeHandler:
    _charge_repository: ChargeRepository

    def __init__(self, charge_repository: ChargeRepository):
        self._charge_repository = charge_repository

    def create(self, command: CreateChargeCommand):
        self._charge_repository.insert(
            Charge(
                id=0,
                enrollment=command.enrollment,
                type_id=ChargeType.enrolment_free,
                situation_id=ChargeSituation.a_receber,
                solicitation_code=command.solicitation_code,
                your_number=command.your_number,
                our_number=command.our_number,
                received_datetime=dt.now(),
                received_value=command.received_value,
                payment_origin=command.payment_origin,
                bar_code=command.bar_code,
                typed_code=command.typed_code,
                txid=command.txid,
                simple_pix_code=command.simple_pix_code,
            )
        )
