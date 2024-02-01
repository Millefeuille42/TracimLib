import json
from abc import ABC, abstractmethod
from typing import Any, Dict


class IModel(ABC):
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]: ...

    @classmethod
    @abstractmethod
    def from_dict(cls, data: Dict[str, Any]) -> object: ...

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    def __str__(self) -> str:
        return self.to_json()

    @classmethod
    def from_json(cls, data: str) -> object:
        return cls.from_dict(json.loads(data))
