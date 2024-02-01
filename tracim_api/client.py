from typing import Optional

import requests

from tracim_api.models.credentials import Credentials
from tracim_api.models.user import User


class MissingIDError(ValueError):
    def __init__(self):
        super().__init__("provide at least an email or a username")


class TracimApiClient:
    protocol: str = "https"
    port: int = 443
    host: str
    session: requests.Session

    def __init__(
        self,
        host: str,
        protocol: str = "https",
        port: int = 443,
    ):
        self.host = host
        self.protocol = protocol
        self.port = port
        self.session = requests.Session()

    @property
    def url(self) -> str:
        return f"{self.protocol}://{self.host}:{self.port}"

    @staticmethod
    def _do_json_request(
        session, url, method, data: Optional[str]
    ) -> requests.Response:
        headers = {
            "Content-type": "application/json",
            "Accept": "application/json",
        }
        response = session.request(
            url=url, method=method, data=data, headers=headers
        )
        response.raise_for_status()
        return response

    def request(
        self, method: str, endpoint: str, data: Optional[str]
    ) -> requests.Response:
        url = self.url + endpoint
        return self._do_json_request(self.session, url, method, data)

    def auth(
        self,
        password: str,
        username: Optional[str] = None,
        email: Optional[str] = None,
    ) -> User:
        if not username and not email:
            raise MissingIDError()
        response = self.request(
            "post",
            "/api/auth/login",
            data=Credentials(
                username=username, email=email, password=password
            ).to_json(),
        )
        return User.from_dict(response.json())
