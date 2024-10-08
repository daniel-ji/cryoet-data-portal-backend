"""
Pydantic validator for DepositionType

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/validators/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long


import uuid

from pydantic import BaseModel, ConfigDict, Field
from support.enums import deposition_types_enum
from typing_extensions import Annotated


class DepositionTypeCreateInputValidator(BaseModel):
    # Pydantic stuff
    model_config = ConfigDict(from_attributes=True)
    deposition_id: Annotated[uuid.UUID | None, Field()]
    type: Annotated[deposition_types_enum | None, Field()]
    id: Annotated[int, Field()]


class DepositionTypeUpdateInputValidator(BaseModel):
    # Pydantic stuff
    model_config = ConfigDict(from_attributes=True)
    deposition_id: Annotated[uuid.UUID | None, Field()]
    type: Annotated[deposition_types_enum | None, Field()]
    id: Annotated[int | None, Field()]
