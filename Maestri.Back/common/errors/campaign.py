from services.common.default_request import ErrorResponse


class PixSlipCampaignError:
    invalid_fields = ErrorResponse(
        400, {"details": "Invalid fields in Payment Creation"}
    )
    not_found = ErrorResponse(404, {"details": "Not Found"})
    user_not_found = ErrorResponse(404, {"details": "User Not Found"})
    client_not_found = ErrorResponse(404, {"details": "Client Not Found"})
    enrollment_not_found = ErrorResponse(404, {"details": "Enrollment Not Found"})
