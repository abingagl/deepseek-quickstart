from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    ADMIN = "admin"
    OWNER = "owner"
    OPERATOR = "operator"
    USER = "user"


class Sensitivity(str, Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    CONFIDENTIAL = "confidential"


class User(BaseModel):
    id: str
    role: Role


class Agent(BaseModel):
    id: str
    name: str
    owner_id: str
    sensitivity: Sensitivity