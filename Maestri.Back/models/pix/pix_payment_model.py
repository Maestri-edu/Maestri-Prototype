from dataclasses import dataclass
from common.enums.person_enums import PersonType


@dataclass(frozen=True, order=True)
class Value:
    original_value: float
    alter_model: int

    def json_request_body(self):
        return {
            "original": str(self.original_value),
            "modalidadeAlteracao": self.alter_model,
        }


@dataclass(frozen=True, order=True)
class Calendar:
    expire_seconds: int

    def json_request_body(self):
        return {"expiracao": self.expire_seconds}


@dataclass(frozen=True, order=True)
class Debtor:
    id_code: str
    name: str
    type: PersonType

    def json_request_body(self):
        return {
            f"{PersonType.get_field_dict()[self.type]}": self.id_code,
            "nome": self.name,
        }


@dataclass(frozen=True, order=True)
class AdicionalInfo:
    name: str
    value: str


@dataclass(frozen=True, order=True)
class PixPaymentModel:
    debtor: Debtor
    value: Value
    calendar: Calendar
    key: str
    solicitation: str

    def json_request_body(self):
        return {
            "calendario": self.calendar.json_request_body(),
            "devedor": self.debtor.json_request_body(),
            "valor": self.value.json_request_body(),
            "chave": self.key,
            "solicitacaoPagador": self.solicitation,
            "infoAdicionais": [],
        }
