import uuid
from dataclasses import field
from datetime import datetime

import strawberry


@strawberry.input
class OrganizationInput:
    id: uuid.UUID | None = None
    name: str | None = None
    organization_type: str | None = None
    users: list[uuid.UUID] | None = field(default_factory=list)
