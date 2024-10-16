import logging
import uuid
from typing import Optional

import strawberry
from strawberry.types import Info

from app.graphql.v1.scalars import OrganizationScalar

logger = logging.getLogger(__name__)


@strawberry.type
class Query:
    @strawberry.field()
    async def organizations(self, info: Info) -> list[OrganizationScalar]:
        return []
