from dataclasses import dataclass
from common.enums.person_enums import PersonType, UF


@dataclass(frozen=True, order=True)
class Telephone:
    ddd: str
    number: str

    def get_complete_number(self) -> str:
        return f"{self.ddd} {self.number}"


@dataclass(frozen=True, order=True)
class Address:
    cep_number: str
    complete_adress: str
    uf: UF
    city: str
    neighborhood: str
    number: str
    complement: str


@dataclass(frozen=True, order=True)
class PayerModel:
    id_number: str
    name: str
    email: str
    type: PersonType
    telephone: Telephone
    adress: Address

    def json_request_body(self):
        return {
            "email": self.email,
            "ddd": self.telephone.ddd,
            "telefone": self.telephone.number,
            "numero": self.adress.number,
            "complemento": self.adress.complement,
            "cpfCnpj": self.id_number,
            "tipoPessoa": self.type.value,
            "nome": self.name,
            "endereco": self.adress.complete_adress,
            "bairro": self.adress.neighborhood,
            "cidade": self.adress.city,
            "uf": self.adress.uf.name,
            "cep": self.adress.cep_number,
        }
