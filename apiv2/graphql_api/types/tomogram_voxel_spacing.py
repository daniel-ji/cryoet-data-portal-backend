"""
GraphQL type for TomogramVoxelSpacing

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/graphql_api/types/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long


import datetime
import enum
import typing
from typing import TYPE_CHECKING, Annotated, Optional, Sequence

import database.models as db
import strawberry
from fastapi import Depends
from graphql_api.helpers.tomogram_voxel_spacing import (
    TomogramVoxelSpacingGroupByOptions,
    build_tomogram_voxel_spacing_groupby_output,
)
from graphql_api.types.annotation_file import AnnotationFileAggregate, format_annotation_file_aggregate_output
from graphql_api.types.tomogram import TomogramAggregate, format_tomogram_aggregate_output
from sqlalchemy import inspect
from sqlalchemy.engine.row import RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry import relay
from strawberry.types import Info
from support.limit_offset import LimitOffsetClause
from typing_extensions import TypedDict
from validators.tomogram_voxel_spacing import (
    TomogramVoxelSpacingCreateInputValidator,
    TomogramVoxelSpacingUpdateInputValidator,
)

from platformics.graphql_api.core.deps import get_authz_client, get_db_session, is_system_user, require_auth_principal
from platformics.graphql_api.core.errors import PlatformicsError
from platformics.graphql_api.core.query_builder import get_aggregate_db_rows, get_db_rows
from platformics.graphql_api.core.query_input_types import (
    FloatComparators,
    IntComparators,
    StrComparators,
    aggregator_map,
    orderBy,
)
from platformics.graphql_api.core.relay_interface import EntityInterface
from platformics.graphql_api.core.strawberry_extensions import DependencyExtension
from platformics.security.authorization import AuthzAction, AuthzClient, Principal

E = typing.TypeVar("E")
T = typing.TypeVar("T")

if TYPE_CHECKING:
    from graphql_api.types.annotation_file import AnnotationFile, AnnotationFileOrderByClause, AnnotationFileWhereClause
    from graphql_api.types.run import Run, RunOrderByClause, RunWhereClause
    from graphql_api.types.tomogram import Tomogram, TomogramOrderByClause, TomogramWhereClause

    pass
else:
    AnnotationFileWhereClause = "AnnotationFileWhereClause"
    AnnotationFile = "AnnotationFile"
    AnnotationFileOrderByClause = "AnnotationFileOrderByClause"
    RunWhereClause = "RunWhereClause"
    Run = "Run"
    RunOrderByClause = "RunOrderByClause"
    TomogramWhereClause = "TomogramWhereClause"
    Tomogram = "Tomogram"
    TomogramOrderByClause = "TomogramOrderByClause"
    pass


"""
------------------------------------------------------------------------------
Dataloaders
------------------------------------------------------------------------------
These are batching functions for loading related objects to avoid N+1 queries.
"""


@relay.connection(
    relay.ListConnection[
        Annotated["AnnotationFile", strawberry.lazy("graphql_api.types.annotation_file")]
    ],  # type:ignore
)
async def load_annotation_file_rows(
    root: "TomogramVoxelSpacing",
    info: Info,
    where: Annotated["AnnotationFileWhereClause", strawberry.lazy("graphql_api.types.annotation_file")] | None = None,
    order_by: Optional[
        list[Annotated["AnnotationFileOrderByClause", strawberry.lazy("graphql_api.types.annotation_file")]]
    ] = [],
) -> Sequence[Annotated["AnnotationFile", strawberry.lazy("graphql_api.types.annotation_file")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.TomogramVoxelSpacing)
    relationship = mapper.relationships["annotation_files"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_annotation_file_aggregate_rows(
    root: "TomogramVoxelSpacing",
    info: Info,
    where: Annotated["AnnotationFileWhereClause", strawberry.lazy("graphql_api.types.annotation_file")] | None = None,
) -> Optional[Annotated["AnnotationFileAggregate", strawberry.lazy("graphql_api.types.annotation_file")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.TomogramVoxelSpacing)
    relationship = mapper.relationships["annotation_files"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_annotation_file_aggregate_output(rows)
    return aggregate_output


@strawberry.field
async def load_run_rows(
    root: "TomogramVoxelSpacing",
    info: Info,
    where: Annotated["RunWhereClause", strawberry.lazy("graphql_api.types.run")] | None = None,
    order_by: Optional[list[Annotated["RunOrderByClause", strawberry.lazy("graphql_api.types.run")]]] = [],
) -> Optional[Annotated["Run", strawberry.lazy("graphql_api.types.run")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.TomogramVoxelSpacing)
    relationship = mapper.relationships["run"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.run_id)  # type:ignore


@relay.connection(
    relay.ListConnection[Annotated["Tomogram", strawberry.lazy("graphql_api.types.tomogram")]],  # type:ignore
)
async def load_tomogram_rows(
    root: "TomogramVoxelSpacing",
    info: Info,
    where: Annotated["TomogramWhereClause", strawberry.lazy("graphql_api.types.tomogram")] | None = None,
    order_by: Optional[list[Annotated["TomogramOrderByClause", strawberry.lazy("graphql_api.types.tomogram")]]] = [],
) -> Sequence[Annotated["Tomogram", strawberry.lazy("graphql_api.types.tomogram")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.TomogramVoxelSpacing)
    relationship = mapper.relationships["tomograms"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_tomogram_aggregate_rows(
    root: "TomogramVoxelSpacing",
    info: Info,
    where: Annotated["TomogramWhereClause", strawberry.lazy("graphql_api.types.tomogram")] | None = None,
) -> Optional[Annotated["TomogramAggregate", strawberry.lazy("graphql_api.types.tomogram")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.TomogramVoxelSpacing)
    relationship = mapper.relationships["tomograms"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_tomogram_aggregate_output(rows)
    return aggregate_output


"""
------------------------------------------------------------------------------
Define Strawberry GQL types
------------------------------------------------------------------------------
"""


"""
Only let users specify IDs in WHERE clause when mutating data (for safety).
We can extend that list as we gather more use cases from the FE team.
"""


@strawberry.input
class TomogramVoxelSpacingWhereClauseMutations(TypedDict):
    id: IntComparators | None


"""
Supported WHERE clause attributes
"""


@strawberry.input
class TomogramVoxelSpacingWhereClause(TypedDict):
    annotation_files: (
        Optional[Annotated["AnnotationFileWhereClause", strawberry.lazy("graphql_api.types.annotation_file")]] | None
    )
    run: Optional[Annotated["RunWhereClause", strawberry.lazy("graphql_api.types.run")]] | None
    tomograms: Optional[Annotated["TomogramWhereClause", strawberry.lazy("graphql_api.types.tomogram")]] | None
    voxel_spacing: Optional[FloatComparators] | None
    s3_prefix: Optional[StrComparators] | None
    https_prefix: Optional[StrComparators] | None
    id: Optional[IntComparators] | None


"""
Supported ORDER BY clause attributes
"""


@strawberry.input
class TomogramVoxelSpacingOrderByClause(TypedDict):
    run: Optional[Annotated["RunOrderByClause", strawberry.lazy("graphql_api.types.run")]] | None
    voxel_spacing: Optional[orderBy] | None
    s3_prefix: Optional[orderBy] | None
    https_prefix: Optional[orderBy] | None
    id: Optional[orderBy] | None


"""
Define TomogramVoxelSpacing type
"""


@strawberry.type(description="Voxel spacings for a run")
class TomogramVoxelSpacing(EntityInterface):
    annotation_files: Sequence[Annotated["AnnotationFile", strawberry.lazy("graphql_api.types.annotation_file")]] = (
        load_annotation_file_rows
    )  # type:ignore
    annotation_files_aggregate: Optional[
        Annotated["AnnotationFileAggregate", strawberry.lazy("graphql_api.types.annotation_file")]
    ] = load_annotation_file_aggregate_rows  # type:ignore
    run: Optional[Annotated["Run", strawberry.lazy("graphql_api.types.run")]] = load_run_rows  # type:ignore
    run_id: Optional[int]
    tomograms: Sequence[Annotated["Tomogram", strawberry.lazy("graphql_api.types.tomogram")]] = (
        load_tomogram_rows
    )  # type:ignore
    tomograms_aggregate: Optional[Annotated["TomogramAggregate", strawberry.lazy("graphql_api.types.tomogram")]] = (
        load_tomogram_aggregate_rows
    )  # type:ignore
    voxel_spacing: float = strawberry.field(description="Voxel spacing equal in all three axes in angstroms")
    s3_prefix: str = strawberry.field(description="Path to a directory containing data for this entity as an S3 url")
    https_prefix: str = strawberry.field(
        description="Path to a directory containing data for this entity as an HTTPS url",
    )
    id: int = strawberry.field(description="An identifier to refer to a specific instance of this type")


"""
We need to add this to each Queryable type so that strawberry will accept either our
Strawberry type *or* a SQLAlchemy model instance as a valid response class from a resolver
"""
TomogramVoxelSpacing.__strawberry_definition__.is_type_of = (  # type: ignore
    lambda obj, info: type(obj) == db.TomogramVoxelSpacing or type(obj) == TomogramVoxelSpacing
)

"""
------------------------------------------------------------------------------
Aggregation types
------------------------------------------------------------------------------
"""
"""
Define columns that support numerical aggregations
"""


@strawberry.type
class TomogramVoxelSpacingNumericalColumns:
    voxel_spacing: Optional[float] = None
    id: Optional[int] = None


"""
Define columns that support min/max aggregations
"""


@strawberry.type
class TomogramVoxelSpacingMinMaxColumns:
    voxel_spacing: Optional[float] = None
    s3_prefix: Optional[str] = None
    https_prefix: Optional[str] = None
    id: Optional[int] = None


"""
Define enum of all columns to support count and count(distinct) aggregations
"""


@strawberry.enum
class TomogramVoxelSpacingCountColumns(enum.Enum):
    annotationFiles = "annotation_files"
    run = "run"
    tomograms = "tomograms"
    voxelSpacing = "voxel_spacing"
    s3Prefix = "s3_prefix"
    httpsPrefix = "https_prefix"
    id = "id"


"""
All supported aggregation functions
"""


@strawberry.type
class TomogramVoxelSpacingAggregateFunctions:
    # This is a hack to accept "distinct" and "columns" as arguments to "count"
    @strawberry.field
    def count(
        self, distinct: Optional[bool] = False, columns: Optional[TomogramVoxelSpacingCountColumns] = None,
    ) -> Optional[int]:
        # Count gets set with the proper value in the resolver, so we just return it here
        return self.count  # type: ignore

    sum: Optional[TomogramVoxelSpacingNumericalColumns] = None
    avg: Optional[TomogramVoxelSpacingNumericalColumns] = None
    stddev: Optional[TomogramVoxelSpacingNumericalColumns] = None
    variance: Optional[TomogramVoxelSpacingNumericalColumns] = None
    min: Optional[TomogramVoxelSpacingMinMaxColumns] = None
    max: Optional[TomogramVoxelSpacingMinMaxColumns] = None
    groupBy: Optional[TomogramVoxelSpacingGroupByOptions] = None


"""
Wrapper around TomogramVoxelSpacingAggregateFunctions
"""


@strawberry.type
class TomogramVoxelSpacingAggregate:
    aggregate: Optional[list[TomogramVoxelSpacingAggregateFunctions]] = None


"""
------------------------------------------------------------------------------
Mutation types
------------------------------------------------------------------------------
"""


@strawberry.input()
class TomogramVoxelSpacingCreateInput:
    run_id: Optional[strawberry.ID] = strawberry.field(description=None, default=None)
    voxel_spacing: float = strawberry.field(description="Voxel spacing equal in all three axes in angstroms")
    s3_prefix: str = strawberry.field(description="Path to a directory containing data for this entity as an S3 url")
    https_prefix: str = strawberry.field(
        description="Path to a directory containing data for this entity as an HTTPS url",
    )
    id: int = strawberry.field(description="An identifier to refer to a specific instance of this type")


@strawberry.input()
class TomogramVoxelSpacingUpdateInput:
    run_id: Optional[strawberry.ID] = strawberry.field(description=None, default=None)
    voxel_spacing: Optional[float] = strawberry.field(description="Voxel spacing equal in all three axes in angstroms")
    s3_prefix: Optional[str] = strawberry.field(
        description="Path to a directory containing data for this entity as an S3 url",
    )
    https_prefix: Optional[str] = strawberry.field(
        description="Path to a directory containing data for this entity as an HTTPS url",
    )
    id: Optional[int] = strawberry.field(description="An identifier to refer to a specific instance of this type")


"""
------------------------------------------------------------------------------
Utilities
------------------------------------------------------------------------------
"""


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_tomogram_voxel_spacings(
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[TomogramVoxelSpacingWhereClause] = None,
    order_by: Optional[list[TomogramVoxelSpacingOrderByClause]] = [],
    limit_offset: Optional[LimitOffsetClause] = None,
) -> typing.Sequence[TomogramVoxelSpacing]:
    """
    Resolve TomogramVoxelSpacing objects. Used for queries (see graphql_api/queries.py).
    """
    limit = limit_offset["limit"] if limit_offset and "limit" in limit_offset else None
    offset = limit_offset["offset"] if limit_offset and "offset" in limit_offset else None
    if offset and not limit:
        raise PlatformicsError("Cannot use offset without limit")
    return await get_db_rows(db.TomogramVoxelSpacing, session, authz_client, principal, where, order_by, AuthzAction.VIEW, limit, offset)  # type: ignore


def format_tomogram_voxel_spacing_aggregate_output(
    query_results: Sequence[RowMapping] | RowMapping,
) -> TomogramVoxelSpacingAggregate:
    """
    Given a row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    aggregate = []
    if type(query_results) is not list:
        query_results = [query_results]  # type: ignore
    for row in query_results:
        aggregate.append(format_tomogram_voxel_spacing_aggregate_row(row))
    return TomogramVoxelSpacingAggregate(aggregate=aggregate)


def format_tomogram_voxel_spacing_aggregate_row(row: RowMapping) -> TomogramVoxelSpacingAggregateFunctions:
    """
    Given a single row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    output = TomogramVoxelSpacingAggregateFunctions()
    for key, value in row.items():
        # Key is either an aggregate function or a groupby key
        group_keys = key.split(".")
        aggregate = key.split("_", 1)
        if aggregate[0] not in aggregator_map.keys():
            # Turn list of groupby keys into nested objects
            if not output.groupBy:
                output.groupBy = TomogramVoxelSpacingGroupByOptions()
            group = build_tomogram_voxel_spacing_groupby_output(output.groupBy, group_keys, value)
            output.groupBy = group
        else:
            aggregate_name = aggregate[0]
            if aggregate_name == "count":
                output.count = value
            else:
                aggregator_fn, col_name = aggregate[0], aggregate[1]
                if not getattr(output, aggregator_fn):
                    if aggregate_name in ["min", "max"]:
                        setattr(output, aggregator_fn, TomogramVoxelSpacingMinMaxColumns())
                    else:
                        setattr(output, aggregator_fn, TomogramVoxelSpacingNumericalColumns())
                setattr(getattr(output, aggregator_fn), col_name, value)
    return output


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_tomogram_voxel_spacings_aggregate(
    info: Info,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[TomogramVoxelSpacingWhereClause] = None,
    # TODO: add support for groupby, limit/offset
) -> TomogramVoxelSpacingAggregate:
    """
    Aggregate values for TomogramVoxelSpacing objects. Used for queries (see graphql_api/queries.py).
    """
    # Get the selected aggregate functions and columns to operate on, and groupby options if any were provided.
    # TODO: not sure why selected_fields is a list
    selections = info.selected_fields[0].selections[0].selections
    aggregate_selections = [selection for selection in selections if selection.name != "groupBy"]
    groupby_selections = [selection for selection in selections if selection.name == "groupBy"]
    groupby_selections = groupby_selections[0].selections if groupby_selections else []

    if not aggregate_selections:
        raise PlatformicsError("No aggregate functions selected")

    rows = await get_aggregate_db_rows(db.TomogramVoxelSpacing, session, authz_client, principal, where, aggregate_selections, [], groupby_selections)  # type: ignore
    aggregate_output = format_tomogram_voxel_spacing_aggregate_output(rows)
    return aggregate_output


@strawberry.mutation(extensions=[DependencyExtension()])
async def create_tomogram_voxel_spacing(
    input: TomogramVoxelSpacingCreateInput,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> db.TomogramVoxelSpacing:
    """
    Create a new TomogramVoxelSpacing object. Used for mutations (see graphql_api/mutations.py).
    """
    validated = TomogramVoxelSpacingCreateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Validate that the user can read all of the entities they're linking to.

    # Validate that the user can read all of the entities they're linking to.
    # Check that run relationship is accessible.
    if validated.run_id:
        run = await get_db_rows(
            db.Run, session, authz_client, principal, {"id": {"_eq": validated.run_id}}, [], AuthzAction.VIEW,
        )
        if not run:
            raise PlatformicsError("Unauthorized: run does not exist")

    # Save to DB
    params["owner_user_id"] = int(principal.id)
    new_entity = db.TomogramVoxelSpacing(**params)

    # Are we actually allowed to create this entity?
    if not authz_client.can_create(new_entity, principal):
        raise PlatformicsError("Unauthorized: Cannot create entity")

    session.add(new_entity)
    await session.commit()
    return new_entity


@strawberry.mutation(extensions=[DependencyExtension()])
async def update_tomogram_voxel_spacing(
    input: TomogramVoxelSpacingUpdateInput,
    where: TomogramVoxelSpacingWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> Sequence[db.TomogramVoxelSpacing]:
    """
    Update TomogramVoxelSpacing objects. Used for mutations (see graphql_api/mutations.py).
    """
    validated = TomogramVoxelSpacingUpdateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Need at least one thing to update
    num_params = len([x for x in params if params[x] is not None])
    if num_params == 0:
        raise PlatformicsError("No fields to update")

    # Validate that the user can read all of the entities they're linking to.
    # Check that run relationship is accessible.
    if validated.run_id:
        run = await get_db_rows(
            db.Run, session, authz_client, principal, {"id": {"_eq": validated.run_id}}, [], AuthzAction.VIEW,
        )
        if not run:
            raise PlatformicsError("Unauthorized: run does not exist")
        params["run"] = run[0]
        del params["run_id"]

    # Fetch entities for update, if we have access to them
    entities = await get_db_rows(
        db.TomogramVoxelSpacing, session, authz_client, principal, where, [], AuthzAction.UPDATE,
    )
    if len(entities) == 0:
        raise PlatformicsError("Unauthorized: Cannot update entities")

    # Update DB
    updated_at = datetime.datetime.now()
    for entity in entities:
        entity.updated_at = updated_at
        for key in params:
            if params[key] is not None:
                setattr(entity, key, params[key])

    if not authz_client.can_update(entity, principal):
        raise PlatformicsError("Unauthorized: Cannot access new collection")

    await session.commit()
    return entities


@strawberry.mutation(extensions=[DependencyExtension()])
async def delete_tomogram_voxel_spacing(
    where: TomogramVoxelSpacingWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
) -> Sequence[db.TomogramVoxelSpacing]:
    """
    Delete TomogramVoxelSpacing objects. Used for mutations (see graphql_api/mutations.py).
    """
    # Fetch entities for deletion, if we have access to them
    entities = await get_db_rows(
        db.TomogramVoxelSpacing, session, authz_client, principal, where, [], AuthzAction.DELETE,
    )
    if len(entities) == 0:
        raise PlatformicsError("Unauthorized: Cannot delete entities")

    # Update DB
    for entity in entities:
        await session.delete(entity)
    await session.commit()
    return entities