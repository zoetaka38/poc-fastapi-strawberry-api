import uuid
from dataclasses import field
from datetime import date, datetime

import strawberry
from pydantic import Field, typing


@strawberry.type
class OperationNotAllowed:
    message: str = "Operation not allowed"


@strawberry.type
class OrganizationScalar:
    id: uuid.UUID
    name: str | None = ""
    users: list["OrganizationUser"] | None = field(default_factory=list)
    created_at: datetime | None = ""
    updated_at: datetime | None = ""


@strawberry.type
class OrganizationUser:
    id: uuid.UUID
    name: str | None = ""
    email: str | None = ""


@strawberry.type
class UserScalar:
    id: uuid.UUID
    name: str | None = ""
    email: str | None = ""
    email_verified: bool | None = False
    policies: list[str] | None = ""
    created_at: datetime | None = ""
    updated_at: datetime | None = ""
    deleted_at: datetime | None = ""
