import strawberry


@strawberry.type
class OrganizationNotFound:
    message: str = "Couldn't find project with the supplied id"


@strawberry.type
class OrganizationIdMissing:
    message: str = "Please supply project id"


@strawberry.type
class OrganizationDeleted:
    message: str = "Organization deleted"
