"""
Factory for generating TomogramVoxelSpacing objects.

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/test_infra/factories/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long

import random
import factory
import uuid6
from database.models import TomogramVoxelSpacing
from platformics.test_infra.factories.base import FileFactory, CommonFactory
from test_infra.factories.run import RunFactory
from factory import Faker, fuzzy
from faker_biology.bioseq import Bioseq
from faker_biology.physiology import Organ
from faker_enum import EnumProvider

Faker.add_provider(Bioseq)
Faker.add_provider(Organ)
Faker.add_provider(EnumProvider)


class TomogramVoxelSpacingFactory(CommonFactory):
    class Meta:
        sqlalchemy_session = None  # workaround for a bug in factoryboy
        model = TomogramVoxelSpacing

        sqlalchemy_get_or_create = ("id",)

    run = factory.SubFactory(
        RunFactory,
    )
    voxel_spacing = fuzzy.FuzzyFloat(1, 100)
    s3_prefix = fuzzy.FuzzyText()
    https_prefix = fuzzy.FuzzyText()
    id = fuzzy.FuzzyInteger(1, 1000)
