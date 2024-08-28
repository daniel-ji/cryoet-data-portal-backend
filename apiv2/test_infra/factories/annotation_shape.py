"""
Factory for generating AnnotationShape objects.

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/test_infra/factories/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long

import factory
from database.models import AnnotationShape
from factory import Faker, fuzzy
from faker_biology.bioseq import Bioseq
from faker_biology.physiology import Organ
from faker_enum import EnumProvider
from platformics.test_infra.factories.base import CommonFactory

from test_infra.factories.annotation import AnnotationFactory

Faker.add_provider(Bioseq)
Faker.add_provider(Organ)
Faker.add_provider(EnumProvider)


class AnnotationShapeFactory(CommonFactory):
    class Meta:
        sqlalchemy_session = None  # workaround for a bug in factoryboy
        model = AnnotationShape

        sqlalchemy_get_or_create = ("id",)

    annotation = factory.SubFactory(
        AnnotationFactory,
    )
    shape_type = fuzzy.FuzzyChoice(["SegmentationMask", "OrientedPoint", "Point", "InstanceSegmentation"])
    id = fuzzy.FuzzyInteger(1, 1000)
