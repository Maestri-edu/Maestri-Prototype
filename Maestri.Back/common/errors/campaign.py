from services.common.default_request import ErrorResponse


class PixSlipCampaignError:
    invalid_fields = ErrorResponse(
        400, {"details": "Invalid fields in Payment Creation"}
    )
