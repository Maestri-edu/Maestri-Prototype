import requests
from dataclasses import dataclass
from common.constants.web_constants import URL
from common.enums.request_type import RequestType


@dataclass(frozen=True, order=True)
class _TestResponse:
    status_code: int
    request: str
    token: str = "Bearer ABCDEFGHIJKMLNOPQRSTUVWXYZ - Token"


class DefaultRequest:
    _request_dict = {
        RequestType.GET: requests.get,
        RequestType.POST: requests.post,
        RequestType.PUT: requests.put,
        RequestType.DELETE: requests.delete,
        RequestType.PATCH: requests.patch,
    }

    def type_request(
        self,
        type: RequestType,
        url: URL,
        header: dict[str, str],
        body: dict[str, str | int | float] | str,
    ):
        request = f"type: {type.name} url: {url} header: {header} body: {body}"

        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {body}")
        print("------------------------------")
        print("\n")

        response = _TestResponse(200, request)

        return response

        """ Commented For Testing """

        # typed_request = self._request_dict[type]

        # response : requests.Response = typed_request(
        #     url.value,
        #     headers = header,
        #     data = body
        # )

        # response.raise_for_status()

        # return response
