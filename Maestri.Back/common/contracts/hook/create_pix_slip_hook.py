from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class CreatePixSlipWebHook:
    hook_url: str

    @staticmethod
    def create(data: dict):
        return CreatePixSlipWebHook(hook_url=data["hookUrl"])
