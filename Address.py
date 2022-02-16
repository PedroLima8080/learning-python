from urllib.error import HTTPError
from urllib.request import urlopen, Request
import json;

class Address:
    _zipCode = None;
    _baseUrl = "https://viacep.com.br/ws/:zip_code/json/"

    def __init__(self, zip_code):
        self._zipCode = zip_code;

    def getAddressByApi(self):
        if not self._baseUrl.startswith("http"):
            raise RuntimeError("Incorrect and possibly insecure protocol in url")

        url = self._baseUrl.replace(':zip_code', self._zipCode);
        httprequest = Request(url, headers={"Accept": "application/json"})

        try:
            with urlopen(httprequest) as response:
                if response.status == 200:
                    response = response.read().decode()
                    return json.loads(response);
        except (HTTPError):
            return False;
