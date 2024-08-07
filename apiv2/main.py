"""
Launch the GraphQL server.
"""

import strawberry
import uvicorn
from fastapi import Depends

from cerbos.sdk.model import Principal
from graphql_api.mutations import Mutation
from graphql_api.queries import Query
from platformics.graphql_api.core.deps import get_auth_principal, require_auth_principal
from platformics.graphql_api.core.error_handler import HandleErrors
from platformics.graphql_api.setup import get_app, get_strawberry_config
from platformics.settings import APISettings

settings = APISettings.model_validate({})  # Workaround for https://github.com/pydantic/pydantic/issues/3753
schema = strawberry.Schema(query=Query, mutation=Mutation, config=get_strawberry_config(), extensions=[HandleErrors()])


# Create and run app
app = get_app(settings, schema)


def override_auth_principal(principal: Principal = Depends(get_auth_principal)):
    if principal:
        return principal

    # Create an anonymous auth scope if we don't have a logged in user!
    return Principal(
        "anonymous",
        roles=["user"],
        attr={
            "user_id": 0,
            "owner_projects": [],
            "member_projects": [],
            "service_identity": [],
            "viewer_projects": [],
        },
    )


app.dependency_overrides[require_auth_principal] = override_auth_principal

if __name__ == "__main__":
    config = uvicorn.Config("main:app", host="0.0.0.0", port=9008, log_level="info")
    server = uvicorn.Server(config)
    server.run()
