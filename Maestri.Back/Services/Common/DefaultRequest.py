from dataclasses import dataclass
from typing import dataclass_transform
from Common.Constants.WebConstants import URL
import requests
import json

@dataclass(frozen = True, order = True)
class _TestResponse:
    status_code: int
    token: str = "ABCDEFGHIJKMLNOPQRSTUVWXYZ"

class DefaultRequest:
    
    def post_request(self, url: URL, header: dict[str, str], body: dict[str, str | int | float] | str):

        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {json.dumps(body)}")
        print("------------------------------")
        print("\n")
        
        response = _TestResponse(200)

        return response

        # response = requests.post(url.value,
        #     headers = header,
        #     data = body)
        
        # response.raise_for_status()
        # return response
    
    def get_request(self, url: URL, header: str, body: str):
        
        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {json.dumps(body)}")
        print("------------------------------")
        print("\n")

        response = _TestResponse(200)

        return response.status_code
        
        # response = requests.get(url,
        #     headers = {"Content-Type": "application/x-www-form-urlencoded"},
        #     data = body)
        
        # response.raise_for_status()
        
        # return response
