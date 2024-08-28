"""
SQLAlchemy database model for DepositionAuthor

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/database/models/class_name.py.j2 instead.
"""

from typing import TYPE_CHECKING

from platformics.database.models.base import Base
from platformics.database.models.file import File
from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from database.models.deposition import Deposition
    from platformics.database.models.file import File

    ...
else:
    File = "File"
    Deposition = "Deposition"
    ...


class DepositionAuthor(Base):
    __tablename__ = "deposition_author"
    __mapper_args__ = {"polymorphic_identity": __tablename__, "polymorphic_load": "inline"}

    deposition_id: Mapped[int] = mapped_column(Integer, ForeignKey("deposition.id"), nullable=True, index=True)
    deposition: Mapped["Deposition"] = relationship(
        "Deposition",
        foreign_keys=deposition_id,
        back_populates="authors",
    )
    author_list_order: Mapped[int] = mapped_column(Integer, nullable=False)
    orcid: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=True)
    affiliation_name: Mapped[str] = mapped_column(String, nullable=True)
    affiliation_address: Mapped[str] = mapped_column(String, nullable=True)
    affiliation_identifier: Mapped[str] = mapped_column(String, nullable=True)
    corresponding_author_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    primary_author_status: Mapped[bool] = mapped_column(Boolean, nullable=True)
    id: Mapped[int] = mapped_column(Integer, nullable=False, index=True, autoincrement=True, primary_key=True)
