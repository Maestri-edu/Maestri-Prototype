from dataclasses import dataclass
from models.common.payer_model import Telephone


@dataclass(frozen=True, order=True)
class CreateCampaignPixSlipPayment:
    payment_value: float
    payer_id: str
    payer_name: str
    payer_email: str
    payer_cep: str
    payer_telephone: Telephone
    course_id: int
    course_name: str

    @staticmethod
    def create(data: dict):
        return CreateCampaignPixSlipPayment(
            payment_value=data["paymentValue"],
            payer_id=data["payerId"],
            payer_name=data["payerName"],
            payer_email=data["payerEmail"],
            payer_cep=data["payerCep"],
            payer_telephone=Telephone(
                ddd=data["payerTelephoneDDD"], number=data["payerTelephoneNumber"]
            ),
            course_id=data["courseId"],
            course_name=data["courseName"],
        )

    def json_request_body(self):
        return {
            "paymentValue": self.payment_value,
            "payerId": self.payer_id,
            "payerName": self.payer_name,
            "payerEmail": self.payer_email,
            "payerCep": self.payer_cep,
            "payerTelephoneDDD": self.payer_telephone.ddd,
            "payerTelephoneNumber": self.payer_telephone.number,
            "courseId": self.course_id,
            "courseName": self.course_name,
        }
