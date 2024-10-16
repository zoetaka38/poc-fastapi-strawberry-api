import strawberry

from app.graphql.v1.organizations.scalar import (
    OrganizationDeleted,
    OrganizationIdMissing,
    OrganizationNotFound,
)
from app.graphql.v1.scalars import OperationNotAllowed, OrganizationScalar

AddOrganizationScalarResponse = strawberry.union(
    "AddOrganizationScalarResponse",
    (
        OperationNotAllowed,
        OrganizationScalar,
    ),
)
UpdateOrganizationScalarResponse = strawberry.union(
    "UpdateOrganizationScalarResponse",
    (
        OperationNotAllowed,
        OrganizationNotFound,
        OrganizationScalar,
    ),
)
DeleteOrganizationResponse = strawberry.union(
    "DeleteOrganizationResponse",
    (OperationNotAllowed, OrganizationDeleted, OrganizationNotFound, OrganizationIdMissing),
)
