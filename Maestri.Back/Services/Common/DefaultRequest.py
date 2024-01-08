import json
import requests
from dataclasses import dataclass
from Common.Constants.WebConstants import URL

@dataclass(frozen = True, order = True)
class _TestResponse:
    status_code: int
    request: str
    token: str = "Bearer ABCDEFGHIJKMLNOPQRSTUVWXYZ - Token"

class DefaultRequest:
    
    def post_request(self, url: URL, header: dict[str, str], body: dict[str, str | int | float] | str):

        request = f"{url} {header} {body}"
        
        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {body}")
        print("------------------------------")
        print("\n")
        
        response = _TestResponse(200, request)

        return response

        # response = requests.post(url.value,
        #     headers = header,
        #     data = body)
        
        # response.raise_for_status()
        # return response
    
    def get_request(self, url: URL, header: str, body: str):
        
        request = f"{url} {header} {body}"
        
        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {body}")
        print("------------------------------")
        print("\n")
        
        response = _TestResponse(200, request)

        return response
        
        # response = requests.get(url,
        #     headers = {"Content-Type": "application/x-www-form-urlencoded"},
        #     data = body)
        
        # response.raise_for_status()
        
        # return response
    
    def put_request(self, url: URL, header: dict[str, str], body: dict[str, str | int | float] | str):
        
        request = f"{url} {header} {body}"
        
        print("\n")
        print("------------------------------")
        print(f" {url.value} \n\n {header} \n\n {body}")
        print("------------------------------")
        print("\n")
        
        response = _TestResponse(200, request)

        return response
        
        # response = requests.put(url.value,
        #     headers = header,
        #     data = body)
        
        # response.raise_for_status()
        
        # return response
