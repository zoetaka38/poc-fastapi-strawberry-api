import uuid
from datetime import date

import strawberry
from pydantic import typing
from strawberry.types import Info

from app.graphql.v1.inputs import OrganizationInput
from app.graphql.v1.organizations.fragments import AddOrganizationScalarResponse


@strawberry.type
class Mutation:
    @strawberry.mutation()
    async def add_organization(
        self,
        info: Info,
        organization: OrganizationInput,
    ) -> AddOrganizationScalarResponse:  # type: ignore
        return AddOrganizationScalarResponse(
            id=uuid.uuid4(),
            name=organization.name,
            users=[],
            created_at=date.today(),
            updated_at=date.today(),
        )
