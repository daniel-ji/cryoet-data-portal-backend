"""
SQLAlchemy database model for DatasetFunding

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/database/models/class_name.py.j2 instead.
"""

from typing import TYPE_CHECKING

from platformics.database.models.base import Base
from platformics.database.models.file import File
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from database.models.dataset import Dataset
    from platformics.database.models.file import File

    ...
else:
    File = "File"
    Dataset = "Dataset"
    ...


class DatasetFunding(Base):
    __tablename__ = "dataset_funding"
    __mapper_args__ = {"polymorphic_identity": __tablename__, "polymorphic_load": "inline"}

    dataset_id: Mapped[int] = mapped_column(Integer, ForeignKey("dataset.id"), nullable=True, index=True)
    dataset: Mapped["Dataset"] = relationship(
        "Dataset",
        foreign_keys=dataset_id,
        back_populates="funding_sources",
    )
    funding_agency_name: Mapped[str] = mapped_column(String, nullable=True)
    grant_id: Mapped[str] = mapped_column(String, nullable=True)
    id: Mapped[int] = mapped_column(Integer, nullable=False, index=True, autoincrement=True, primary_key=True)
