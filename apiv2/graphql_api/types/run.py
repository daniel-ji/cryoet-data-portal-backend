"""
GraphQL type for Run

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
from graphql_api.helpers.run import RunGroupByOptions, build_run_groupby_output
from graphql_api.types.alignment import AlignmentAggregate, format_alignment_aggregate_output
from graphql_api.types.annotation import AnnotationAggregate, format_annotation_aggregate_output
from graphql_api.types.frame import FrameAggregate, format_frame_aggregate_output
from graphql_api.types.tiltseries import TiltseriesAggregate, format_tiltseries_aggregate_output
from graphql_api.types.tomogram import TomogramAggregate, format_tomogram_aggregate_output
from graphql_api.types.tomogram_voxel_spacing import (
    TomogramVoxelSpacingAggregate,
    format_tomogram_voxel_spacing_aggregate_output,
)
from platformics.graphql_api.core.deps import get_authz_client, get_db_session, is_system_user, require_auth_principal
from platformics.graphql_api.core.errors import PlatformicsError
from platformics.graphql_api.core.query_builder import get_aggregate_db_rows, get_db_rows
from platformics.graphql_api.core.query_input_types import (
    IntComparators,
    StrComparators,
    aggregator_map,
    orderBy,
)
from platformics.graphql_api.core.relay_interface import EntityInterface
from platformics.graphql_api.core.strawberry_extensions import DependencyExtension
from platformics.security.authorization import AuthzAction, AuthzClient, Principal
from sqlalchemy import inspect
from sqlalchemy.engine.row import RowMapping
from sqlalchemy.ext.asyncio import AsyncSession
from strawberry import relay
from strawberry.types import Info
from support.limit_offset import LimitOffsetClause
from typing_extensions import TypedDict
from validators.run import RunCreateInputValidator, RunUpdateInputValidator

E = typing.TypeVar("E")
T = typing.TypeVar("T")

if TYPE_CHECKING:
    from graphql_api.types.alignment import Alignment, AlignmentOrderByClause, AlignmentWhereClause
    from graphql_api.types.annotation import Annotation, AnnotationOrderByClause, AnnotationWhereClause
    from graphql_api.types.dataset import Dataset, DatasetOrderByClause, DatasetWhereClause
    from graphql_api.types.frame import Frame, FrameOrderByClause, FrameWhereClause
    from graphql_api.types.tiltseries import Tiltseries, TiltseriesOrderByClause, TiltseriesWhereClause
    from graphql_api.types.tomogram import Tomogram, TomogramOrderByClause, TomogramWhereClause
    from graphql_api.types.tomogram_voxel_spacing import (
        TomogramVoxelSpacing,
        TomogramVoxelSpacingOrderByClause,
        TomogramVoxelSpacingWhereClause,
    )

    pass
else:
    AlignmentWhereClause = "AlignmentWhereClause"
    Alignment = "Alignment"
    AlignmentOrderByClause = "AlignmentOrderByClause"
    AnnotationWhereClause = "AnnotationWhereClause"
    Annotation = "Annotation"
    AnnotationOrderByClause = "AnnotationOrderByClause"
    DatasetWhereClause = "DatasetWhereClause"
    Dataset = "Dataset"
    DatasetOrderByClause = "DatasetOrderByClause"
    FrameWhereClause = "FrameWhereClause"
    Frame = "Frame"
    FrameOrderByClause = "FrameOrderByClause"
    TiltseriesWhereClause = "TiltseriesWhereClause"
    Tiltseries = "Tiltseries"
    TiltseriesOrderByClause = "TiltseriesOrderByClause"
    TomogramVoxelSpacingWhereClause = "TomogramVoxelSpacingWhereClause"
    TomogramVoxelSpacing = "TomogramVoxelSpacing"
    TomogramVoxelSpacingOrderByClause = "TomogramVoxelSpacingOrderByClause"
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
    relay.ListConnection[Annotated["Alignment", strawberry.lazy("graphql_api.types.alignment")]],  # type:ignore
)
async def load_alignment_rows(
    root: "Run",
    info: Info,
    where: Annotated["AlignmentWhereClause", strawberry.lazy("graphql_api.types.alignment")] | None = None,
    order_by: Optional[list[Annotated["AlignmentOrderByClause", strawberry.lazy("graphql_api.types.alignment")]]] = [],
) -> Sequence[Annotated["Alignment", strawberry.lazy("graphql_api.types.alignment")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["alignments"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_alignment_aggregate_rows(
    root: "Run",
    info: Info,
    where: Annotated["AlignmentWhereClause", strawberry.lazy("graphql_api.types.alignment")] | None = None,
) -> Optional[Annotated["AlignmentAggregate", strawberry.lazy("graphql_api.types.alignment")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["alignments"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_alignment_aggregate_output(rows)
    return aggregate_output


@relay.connection(
    relay.ListConnection[Annotated["Annotation", strawberry.lazy("graphql_api.types.annotation")]],  # type:ignore
)
async def load_annotation_rows(
    root: "Run",
    info: Info,
    where: Annotated["AnnotationWhereClause", strawberry.lazy("graphql_api.types.annotation")] | None = None,
    order_by: Optional[
        list[Annotated["AnnotationOrderByClause", strawberry.lazy("graphql_api.types.annotation")]]
    ] = [],
) -> Sequence[Annotated["Annotation", strawberry.lazy("graphql_api.types.annotation")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["annotations"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_annotation_aggregate_rows(
    root: "Run",
    info: Info,
    where: Annotated["AnnotationWhereClause", strawberry.lazy("graphql_api.types.annotation")] | None = None,
) -> Optional[Annotated["AnnotationAggregate", strawberry.lazy("graphql_api.types.annotation")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["annotations"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_annotation_aggregate_output(rows)
    return aggregate_output


@strawberry.field
async def load_dataset_rows(
    root: "Run",
    info: Info,
    where: Annotated["DatasetWhereClause", strawberry.lazy("graphql_api.types.dataset")] | None = None,
    order_by: Optional[list[Annotated["DatasetOrderByClause", strawberry.lazy("graphql_api.types.dataset")]]] = [],
) -> Optional[Annotated["Dataset", strawberry.lazy("graphql_api.types.dataset")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["dataset"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.dataset_id)  # type:ignore


@relay.connection(
    relay.ListConnection[Annotated["Frame", strawberry.lazy("graphql_api.types.frame")]],  # type:ignore
)
async def load_frame_rows(
    root: "Run",
    info: Info,
    where: Annotated["FrameWhereClause", strawberry.lazy("graphql_api.types.frame")] | None = None,
    order_by: Optional[list[Annotated["FrameOrderByClause", strawberry.lazy("graphql_api.types.frame")]]] = [],
) -> Sequence[Annotated["Frame", strawberry.lazy("graphql_api.types.frame")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["frames"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_frame_aggregate_rows(
    root: "Run",
    info: Info,
    where: Annotated["FrameWhereClause", strawberry.lazy("graphql_api.types.frame")] | None = None,
) -> Optional[Annotated["FrameAggregate", strawberry.lazy("graphql_api.types.frame")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["frames"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_frame_aggregate_output(rows)
    return aggregate_output


@relay.connection(
    relay.ListConnection[Annotated["Tiltseries", strawberry.lazy("graphql_api.types.tiltseries")]],  # type:ignore
)
async def load_tiltseries_rows(
    root: "Run",
    info: Info,
    where: Annotated["TiltseriesWhereClause", strawberry.lazy("graphql_api.types.tiltseries")] | None = None,
    order_by: Optional[
        list[Annotated["TiltseriesOrderByClause", strawberry.lazy("graphql_api.types.tiltseries")]]
    ] = [],
) -> Sequence[Annotated["Tiltseries", strawberry.lazy("graphql_api.types.tiltseries")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["tiltseries"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_tiltseries_aggregate_rows(
    root: "Run",
    info: Info,
    where: Annotated["TiltseriesWhereClause", strawberry.lazy("graphql_api.types.tiltseries")] | None = None,
) -> Optional[Annotated["TiltseriesAggregate", strawberry.lazy("graphql_api.types.tiltseries")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["tiltseries"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_tiltseries_aggregate_output(rows)
    return aggregate_output


@relay.connection(
    relay.ListConnection[
        Annotated["TomogramVoxelSpacing", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]
    ],  # type:ignore
)
async def load_tomogram_voxel_spacing_rows(
    root: "Run",
    info: Info,
    where: (
        Annotated["TomogramVoxelSpacingWhereClause", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")] | None
    ) = None,
    order_by: Optional[
        list[
            Annotated["TomogramVoxelSpacingOrderByClause", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]
        ]
    ] = [],
) -> Sequence[Annotated["TomogramVoxelSpacing", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["tomogram_voxel_spacings"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_tomogram_voxel_spacing_aggregate_rows(
    root: "Run",
    info: Info,
    where: (
        Annotated["TomogramVoxelSpacingWhereClause", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")] | None
    ) = None,
) -> Optional[Annotated["TomogramVoxelSpacingAggregate", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["tomogram_voxel_spacings"]
    rows = await dataloader.aggregate_loader_for(relationship, where, selections).load(root.id)  # type:ignore
    aggregate_output = format_tomogram_voxel_spacing_aggregate_output(rows)
    return aggregate_output


@relay.connection(
    relay.ListConnection[Annotated["Tomogram", strawberry.lazy("graphql_api.types.tomogram")]],  # type:ignore
)
async def load_tomogram_rows(
    root: "Run",
    info: Info,
    where: Annotated["TomogramWhereClause", strawberry.lazy("graphql_api.types.tomogram")] | None = None,
    order_by: Optional[list[Annotated["TomogramOrderByClause", strawberry.lazy("graphql_api.types.tomogram")]]] = [],
) -> Sequence[Annotated["Tomogram", strawberry.lazy("graphql_api.types.tomogram")]]:
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
    relationship = mapper.relationships["tomograms"]
    return await dataloader.loader_for(relationship, where, order_by).load(root.id)  # type:ignore


@strawberry.field
async def load_tomogram_aggregate_rows(
    root: "Run",
    info: Info,
    where: Annotated["TomogramWhereClause", strawberry.lazy("graphql_api.types.tomogram")] | None = None,
) -> Optional[Annotated["TomogramAggregate", strawberry.lazy("graphql_api.types.tomogram")]]:
    selections = info.selected_fields[0].selections[0].selections
    dataloader = info.context["sqlalchemy_loader"]
    mapper = inspect(db.Run)
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
class RunWhereClauseMutations(TypedDict):
    id: IntComparators | None


"""
Supported WHERE clause attributes
"""


@strawberry.input
class RunWhereClause(TypedDict):
    alignments: Optional[Annotated["AlignmentWhereClause", strawberry.lazy("graphql_api.types.alignment")]] | None
    annotations: Optional[Annotated["AnnotationWhereClause", strawberry.lazy("graphql_api.types.annotation")]] | None
    dataset: Optional[Annotated["DatasetWhereClause", strawberry.lazy("graphql_api.types.dataset")]] | None
    frames: Optional[Annotated["FrameWhereClause", strawberry.lazy("graphql_api.types.frame")]] | None
    tiltseries: Optional[Annotated["TiltseriesWhereClause", strawberry.lazy("graphql_api.types.tiltseries")]] | None
    tomogram_voxel_spacings: (
        Optional[
            Annotated["TomogramVoxelSpacingWhereClause", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]
        ]
        | None
    )
    tomograms: Optional[Annotated["TomogramWhereClause", strawberry.lazy("graphql_api.types.tomogram")]] | None
    name: Optional[StrComparators] | None
    s3_prefix: Optional[StrComparators] | None
    https_prefix: Optional[StrComparators] | None
    id: Optional[IntComparators] | None


"""
Supported ORDER BY clause attributes
"""


@strawberry.input
class RunOrderByClause(TypedDict):
    dataset: Optional[Annotated["DatasetOrderByClause", strawberry.lazy("graphql_api.types.dataset")]] | None
    name: Optional[orderBy] | None
    s3_prefix: Optional[orderBy] | None
    https_prefix: Optional[orderBy] | None
    id: Optional[orderBy] | None


"""
Define Run type
"""


@strawberry.type(description=None)
class Run(EntityInterface):
    alignments: Sequence[Annotated["Alignment", strawberry.lazy("graphql_api.types.alignment")]] = (
        load_alignment_rows
    )  # type:ignore
    alignments_aggregate: Optional[Annotated["AlignmentAggregate", strawberry.lazy("graphql_api.types.alignment")]] = (
        load_alignment_aggregate_rows
    )  # type:ignore
    annotations: Sequence[Annotated["Annotation", strawberry.lazy("graphql_api.types.annotation")]] = (
        load_annotation_rows
    )  # type:ignore
    annotations_aggregate: Optional[
        Annotated["AnnotationAggregate", strawberry.lazy("graphql_api.types.annotation")]
    ] = load_annotation_aggregate_rows  # type:ignore
    dataset: Optional[Annotated["Dataset", strawberry.lazy("graphql_api.types.dataset")]] = (
        load_dataset_rows
    )  # type:ignore
    frames: Sequence[Annotated["Frame", strawberry.lazy("graphql_api.types.frame")]] = load_frame_rows  # type:ignore
    frames_aggregate: Optional[Annotated["FrameAggregate", strawberry.lazy("graphql_api.types.frame")]] = (
        load_frame_aggregate_rows
    )  # type:ignore
    tiltseries: Sequence[Annotated["Tiltseries", strawberry.lazy("graphql_api.types.tiltseries")]] = (
        load_tiltseries_rows
    )  # type:ignore
    tiltseries_aggregate: Optional[
        Annotated["TiltseriesAggregate", strawberry.lazy("graphql_api.types.tiltseries")]
    ] = load_tiltseries_aggregate_rows  # type:ignore
    tomogram_voxel_spacings: Sequence[
        Annotated["TomogramVoxelSpacing", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]
    ] = load_tomogram_voxel_spacing_rows  # type:ignore
    tomogram_voxel_spacings_aggregate: Optional[
        Annotated["TomogramVoxelSpacingAggregate", strawberry.lazy("graphql_api.types.tomogram_voxel_spacing")]
    ] = load_tomogram_voxel_spacing_aggregate_rows  # type:ignore
    tomograms: Sequence[Annotated["Tomogram", strawberry.lazy("graphql_api.types.tomogram")]] = (
        load_tomogram_rows
    )  # type:ignore
    tomograms_aggregate: Optional[Annotated["TomogramAggregate", strawberry.lazy("graphql_api.types.tomogram")]] = (
        load_tomogram_aggregate_rows
    )  # type:ignore
    name: str = strawberry.field(description="Name of a run")
    s3_prefix: str = strawberry.field(description="Path to a directory containing data for this entity as an S3 url")
    https_prefix: str = strawberry.field(
        description="Path to a directory containing data for this entity as an HTTPS url",
    )
    id: int = strawberry.field(description="An identifier to refer to a specific instance of this type")


"""
We need to add this to each Queryable type so that strawberry will accept either our
Strawberry type *or* a SQLAlchemy model instance as a valid response class from a resolver
"""
Run.__strawberry_definition__.is_type_of = lambda obj, info: type(obj) == db.Run or type(obj) == Run  # type: ignore

"""
------------------------------------------------------------------------------
Aggregation types
------------------------------------------------------------------------------
"""
"""
Define columns that support numerical aggregations
"""


@strawberry.type
class RunNumericalColumns:
    id: Optional[int] = None


"""
Define columns that support min/max aggregations
"""


@strawberry.type
class RunMinMaxColumns:
    name: Optional[str] = None
    s3_prefix: Optional[str] = None
    https_prefix: Optional[str] = None
    id: Optional[int] = None


"""
Define enum of all columns to support count and count(distinct) aggregations
"""


@strawberry.enum
class RunCountColumns(enum.Enum):
    alignments = "alignments"
    annotations = "annotations"
    dataset = "dataset"
    frames = "frames"
    tiltseries = "tiltseries"
    tomogramVoxelSpacings = "tomogram_voxel_spacings"
    tomograms = "tomograms"
    name = "name"
    s3Prefix = "s3_prefix"
    httpsPrefix = "https_prefix"
    id = "id"


"""
All supported aggregation functions
"""


@strawberry.type
class RunAggregateFunctions:
    # This is a hack to accept "distinct" and "columns" as arguments to "count"
    @strawberry.field
    def count(self, distinct: Optional[bool] = False, columns: Optional[RunCountColumns] = None) -> Optional[int]:
        # Count gets set with the proper value in the resolver, so we just return it here
        return self.count  # type: ignore

    sum: Optional[RunNumericalColumns] = None
    avg: Optional[RunNumericalColumns] = None
    stddev: Optional[RunNumericalColumns] = None
    variance: Optional[RunNumericalColumns] = None
    min: Optional[RunMinMaxColumns] = None
    max: Optional[RunMinMaxColumns] = None
    groupBy: Optional[RunGroupByOptions] = None


"""
Wrapper around RunAggregateFunctions
"""


@strawberry.type
class RunAggregate:
    aggregate: Optional[list[RunAggregateFunctions]] = None


"""
------------------------------------------------------------------------------
Mutation types
------------------------------------------------------------------------------
"""


@strawberry.input()
class RunCreateInput:
    dataset_id: strawberry.ID = strawberry.field(description="An author of a dataset")
    name: str = strawberry.field(description="Name of a run")
    s3_prefix: str = strawberry.field(description="Path to a directory containing data for this entity as an S3 url")
    https_prefix: str = strawberry.field(
        description="Path to a directory containing data for this entity as an HTTPS url",
    )
    id: int = strawberry.field(description="An identifier to refer to a specific instance of this type")


@strawberry.input()
class RunUpdateInput:
    dataset_id: Optional[strawberry.ID] = strawberry.field(description="An author of a dataset")
    name: Optional[str] = strawberry.field(description="Name of a run")
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
async def resolve_runs(
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[RunWhereClause] = None,
    order_by: Optional[list[RunOrderByClause]] = [],
    limit_offset: Optional[LimitOffsetClause] = None,
) -> typing.Sequence[Run]:
    """
    Resolve Run objects. Used for queries (see graphql_api/queries.py).
    """
    limit = limit_offset["limit"] if limit_offset and "limit" in limit_offset else None
    offset = limit_offset["offset"] if limit_offset and "offset" in limit_offset else None
    if offset and not limit:
        raise PlatformicsError("Cannot use offset without limit")
    return await get_db_rows(db.Run, session, authz_client, principal, where, order_by, AuthzAction.VIEW, limit, offset)  # type: ignore


def format_run_aggregate_output(query_results: Sequence[RowMapping] | RowMapping) -> RunAggregate:
    """
    Given a row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    aggregate = []
    if type(query_results) is not list:
        query_results = [query_results]  # type: ignore
    for row in query_results:
        aggregate.append(format_run_aggregate_row(row))
    return RunAggregate(aggregate=aggregate)


def format_run_aggregate_row(row: RowMapping) -> RunAggregateFunctions:
    """
    Given a single row from the DB containing the results of an aggregate query,
    format the results using the proper GraphQL types.
    """
    output = RunAggregateFunctions()
    for key, value in row.items():
        # Key is either an aggregate function or a groupby key
        group_keys = key.split(".")
        aggregate = key.split("_", 1)
        if aggregate[0] not in aggregator_map.keys():
            # Turn list of groupby keys into nested objects
            if not output.groupBy:
                output.groupBy = RunGroupByOptions()
            group = build_run_groupby_output(output.groupBy, group_keys, value)
            output.groupBy = group
        else:
            aggregate_name = aggregate[0]
            if aggregate_name == "count":
                output.count = value
            else:
                aggregator_fn, col_name = aggregate[0], aggregate[1]
                if not getattr(output, aggregator_fn):
                    if aggregate_name in ["min", "max"]:
                        setattr(output, aggregator_fn, RunMinMaxColumns())
                    else:
                        setattr(output, aggregator_fn, RunNumericalColumns())
                setattr(getattr(output, aggregator_fn), col_name, value)
    return output


@strawberry.field(extensions=[DependencyExtension()])
async def resolve_runs_aggregate(
    info: Info,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    where: Optional[RunWhereClause] = None,
    # TODO: add support for groupby, limit/offset
) -> RunAggregate:
    """
    Aggregate values for Run objects. Used for queries (see graphql_api/queries.py).
    """
    # Get the selected aggregate functions and columns to operate on, and groupby options if any were provided.
    # TODO: not sure why selected_fields is a list
    selections = info.selected_fields[0].selections[0].selections
    aggregate_selections = [selection for selection in selections if selection.name != "groupBy"]
    groupby_selections = [selection for selection in selections if selection.name == "groupBy"]
    groupby_selections = groupby_selections[0].selections if groupby_selections else []

    if not aggregate_selections:
        raise PlatformicsError("No aggregate functions selected")

    rows = await get_aggregate_db_rows(db.Run, session, authz_client, principal, where, aggregate_selections, [], groupby_selections)  # type: ignore
    aggregate_output = format_run_aggregate_output(rows)
    return aggregate_output


@strawberry.mutation(extensions=[DependencyExtension()])
async def create_run(
    input: RunCreateInput,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> db.Run:
    """
    Create a new Run object. Used for mutations (see graphql_api/mutations.py).
    """
    validated = RunCreateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Validate that the user can read all of the entities they're linking to.

    # Validate that the user can read all of the entities they're linking to.
    # Check that dataset relationship is accessible.
    if validated.dataset_id:
        dataset = await get_db_rows(
            db.Dataset,
            session,
            authz_client,
            principal,
            {"id": {"_eq": validated.dataset_id}},
            [],
            AuthzAction.VIEW,
        )
        if not dataset:
            raise PlatformicsError("Unauthorized: dataset does not exist")

    # Save to DB
    params["owner_user_id"] = int(principal.id)
    new_entity = db.Run(**params)

    # Are we actually allowed to create this entity?
    if not authz_client.can_create(new_entity, principal):
        raise PlatformicsError("Unauthorized: Cannot create entity")

    session.add(new_entity)
    await session.commit()
    return new_entity


@strawberry.mutation(extensions=[DependencyExtension()])
async def update_run(
    input: RunUpdateInput,
    where: RunWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
    is_system_user: bool = Depends(is_system_user),
) -> Sequence[db.Run]:
    """
    Update Run objects. Used for mutations (see graphql_api/mutations.py).
    """
    validated = RunUpdateInputValidator(**input.__dict__)
    params = validated.model_dump()

    # Need at least one thing to update
    num_params = len([x for x in params if params[x] is not None])
    if num_params == 0:
        raise PlatformicsError("No fields to update")

    # Validate that the user can read all of the entities they're linking to.
    # Check that dataset relationship is accessible.
    if validated.dataset_id:
        dataset = await get_db_rows(
            db.Dataset,
            session,
            authz_client,
            principal,
            {"id": {"_eq": validated.dataset_id}},
            [],
            AuthzAction.VIEW,
        )
        if not dataset:
            raise PlatformicsError("Unauthorized: dataset does not exist")
        params["dataset"] = dataset[0]
        del params["dataset_id"]

    # Fetch entities for update, if we have access to them
    entities = await get_db_rows(db.Run, session, authz_client, principal, where, [], AuthzAction.UPDATE)
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
async def delete_run(
    where: RunWhereClauseMutations,
    session: AsyncSession = Depends(get_db_session, use_cache=False),
    authz_client: AuthzClient = Depends(get_authz_client),
    principal: Principal = Depends(require_auth_principal),
) -> Sequence[db.Run]:
    """
    Delete Run objects. Used for mutations (see graphql_api/mutations.py).
    """
    # Fetch entities for deletion, if we have access to them
    entities = await get_db_rows(db.Run, session, authz_client, principal, where, [], AuthzAction.DELETE)
    if len(entities) == 0:
        raise PlatformicsError("Unauthorized: Cannot delete entities")

    # Update DB
    for entity in entities:
        await session.delete(entity)
    await session.commit()
    return entities
