from services.common.default_request import ErrorResponse


class PersonalDataError:

    _duplicate_email = ErrorResponse(
        status_code=403, data={"data": "O Email já está em uso"}
    )

    _duplicate_cpf = ErrorResponse(
        status_code=403, data={"data": "O CPF já está cadastrado"}
    )
