from dataclasses import dataclass
from typing import Dict, Optional

from tracim_api.interfaces.model import IModel


@dataclass
class Credentials(IModel):
    password: str
    username: Optional[str] = None
    email: Optional[str] = None

    def __init__(
        self, username: Optional[str], email: Optional[str], password: str
    ):
        self.username = username
        self.email = email
        self.password = password

    @classmethod
    def from_dict(cls, data: Dict[str, Optional[str]]) -> "Credentials":
        return cls(
            username=str(data["username"]),
            email=str(data["email"]),
            password=str(data["password"]),
        )

    def to_dict(self) -> Dict[str, Optional[str]]:
        data: Dict[str, Optional[str]] = dict()
        data["username"] = self.username
        data["email"] = self.email
        data["password"] = self.password
        return data
