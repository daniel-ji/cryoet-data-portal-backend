"""
SQLAlchemy database model for Deposition

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/database/models/class_name.py.j2 instead.
"""

import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from platformics.database.models.base import Base
from platformics.database.models.file import File

if TYPE_CHECKING:
    from database.models.alignment import Alignment
    from database.models.annotation import Annotation
    from database.models.dataset import Dataset
    from database.models.deposition_author import DepositionAuthor
    from database.models.deposition_type import DepositionType
    from database.models.frame import Frame
    from database.models.tiltseries import Tiltseries
    from database.models.tomogram import Tomogram

    from platformics.database.models.file import File

    ...
else:
    File = "File"
    DepositionAuthor = "DepositionAuthor"
    Alignment = "Alignment"
    Annotation = "Annotation"
    Dataset = "Dataset"
    Frame = "Frame"
    Tiltseries = "Tiltseries"
    Tomogram = "Tomogram"
    DepositionType = "DepositionType"
    ...


class Deposition(Base):
    __tablename__ = "deposition"
    __mapper_args__ = {"polymorphic_identity": __tablename__, "polymorphic_load": "inline"}

    authors: Mapped[list[DepositionAuthor]] = relationship(
        "DepositionAuthor",
        back_populates="deposition",
        uselist=True,
        foreign_keys="DepositionAuthor.deposition_id",
        cascade="all, delete-orphan",
    )
    alignments: Mapped[list[Alignment]] = relationship(
        "Alignment",
        back_populates="deposition",
        uselist=True,
        foreign_keys="Alignment.deposition_id",
        cascade="all, delete-orphan",
    )
    annotations: Mapped[list[Annotation]] = relationship(
        "Annotation",
        back_populates="deposition",
        uselist=True,
        foreign_keys="Annotation.deposition_id",
        cascade="all, delete-orphan",
    )
    datasets: Mapped[list[Dataset]] = relationship(
        "Dataset",
        back_populates="deposition",
        uselist=True,
        foreign_keys="Dataset.deposition_id",
        cascade="all, delete-orphan",
    )
    frames: Mapped[list[Frame]] = relationship(
        "Frame",
        back_populates="deposition",
        uselist=True,
        foreign_keys="Frame.deposition_id",
        cascade="all, delete-orphan",
    )
    tiltseries: Mapped[list[Tiltseries]] = relationship(
        "Tiltseries",
        back_populates="deposition",
        uselist=True,
        foreign_keys="Tiltseries.deposition_id",
        cascade="all, delete-orphan",
    )
    tomograms: Mapped[list[Tomogram]] = relationship(
        "Tomogram",
        back_populates="deposition",
        uselist=True,
        foreign_keys="Tomogram.deposition_id",
        cascade="all, delete-orphan",
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    tag: Mapped[str] = mapped_column(String, nullable=True)
    deposition_types: Mapped[list[DepositionType]] = relationship(
        "DepositionType",
        back_populates="deposition",
        uselist=True,
        foreign_keys="DepositionType.deposition_id",
        cascade="all, delete-orphan",
    )
    deposition_publications: Mapped[str] = mapped_column(String, nullable=True)
    related_database_entries: Mapped[str] = mapped_column(String, nullable=True)
    deposition_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    release_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    last_modified_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    key_photo_url: Mapped[str] = mapped_column(String, nullable=True)
    key_photo_thumbnail_url: Mapped[str] = mapped_column(String, nullable=True)
    id: Mapped[int] = mapped_column(Integer, nullable=False, index=True, autoincrement=True, primary_key=True)
