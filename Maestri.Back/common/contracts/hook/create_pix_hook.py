from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class CreatePixWebHook:
    hook_url: str

    @staticmethod
    def create(data: dict):
        return CreatePixWebHook(data["hook_url"])
