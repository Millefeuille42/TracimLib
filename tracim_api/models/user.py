import json
from dataclasses import dataclass
from typing import Any, Dict

from tracim_api.interfaces.model import IModel


@dataclass
class User(IModel):
    allowed_space: int
    auth_type: str
    created: str
    email: str
    has_avatar: bool
    has_cover: bool
    is_active: bool
    is_deleted: bool
    lang: str
    profile: str
    public_name: str
    timezone: str
    user_id: int
    username: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        return User(
            allowed_space=int(data["allowed_space"]),
            auth_type=str(data["auth_type"]),
            created=str(data["created"]),
            email=str(data["email"]),
            has_avatar=bool(data["has_avatar"]),
            has_cover=bool(data["has_cover"]),
            is_active=bool(data["is_active"]),
            is_deleted=bool(data["is_deleted"]),
            lang=str(data["lang"]),
            profile=str(data["profile"]),
            public_name=str(data["public_name"]),
            timezone=str(data["timezone"]),
            user_id=int(data["user_id"]),
            username=str(data["username"]),
        )

    @classmethod
    def from_json(cls, data: str) -> "User":
        return User.from_dict(json.loads(data))

    def to_dict(self) -> Dict[str, Any]:
        data: Dict[str, Any] = dict()
        data["allowed_space"] = self.allowed_space
        data["auth_type"] = self.auth_type
        data["created"] = self.created
        data["email"] = self.email
        data["has_avatar"] = self.has_avatar
        data["has_cover"] = self.has_cover
        data["is_active"] = self.is_active
        data["is_deleted"] = self.is_deleted
        data["lang"] = self.lang
        data["profile"] = self.profile
        data["public_name"] = self.public_name
        data["timezone"] = self.timezone
        data["user_id"] = self.user_id
        data["username"] = self.username
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def __str__(self) -> str:
        return self.to_json()
