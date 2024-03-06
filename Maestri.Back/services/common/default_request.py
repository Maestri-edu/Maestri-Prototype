from typing import Any
import requests
from dataclasses import dataclass
from common.constants.web_constants import URL
from common.enums.request_type import RequestType
from result import Ok, Err, Result
from common.secrets.inter.certificates import Certificates
import json

@dataclass(frozen=True, order=True)
class SuccessResponse:
    status_code: int
    data: dict[str, Any]
    success: bool = True


@dataclass(frozen=True, order=True)
class ErrorResponse:
    status_code: int
    data: dict[str, Any]
    success: bool = False


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
    ) -> Result[SuccessResponse, ErrorResponse]:
        request = f"type: {type.name} url: {url.value} header: {header} body: {body}"

        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {body}")
        print("------------------------------")
        print("\n")

        # response = SuccessResponse(
        #     200,
        #     {
        #         "details": request,
        #         "access_token": "- access token token token token access - ",
        #     },
        # )

        #return Ok(response)

        """Commented For Testing"""

        typed_request = self._request_dict[type]

        if isinstance(body, dict):
            data=json.dumps(body)
        else:
            data = body

        response: requests.Response = typed_request(
            url=url.value, headers=header, data=data, cert=(Certificates.Certificate_Path, Certificates.Key_Path)
        )

        try:
            response.raise_for_status()
        except requests.HTTPError as ex:
            return Err(
                ErrorResponse(response.status_code, self._extract_json_data(response))
            )

        mapped_result = SuccessResponse(
            response.status_code, self._extract_json_data(response)
        )

        print(
            "It worked somehow",
            mapped_result.status_code,
            mapped_result.data,
            mapped_result.success,
        )

        return Ok(mapped_result)

    def _extract_json_data(self, response: requests.Response) -> dict[str, Any]:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            return {"details": response.text}
