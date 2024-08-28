"""
Factory for generating PerSectionAlignmentParameters objects.

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/test_infra/factories/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long

import random
import factory
import uuid6
from database.models import PerSectionAlignmentParameters
from platformics.test_infra.factories.base import FileFactory, CommonFactory
from test_infra.factories.alignment import AlignmentFactory
from factory import Faker, fuzzy
from faker_biology.bioseq import Bioseq
from faker_biology.physiology import Organ
from faker_enum import EnumProvider

Faker.add_provider(Bioseq)
Faker.add_provider(Organ)
Faker.add_provider(EnumProvider)


class PerSectionAlignmentParametersFactory(CommonFactory):
    class Meta:
        sqlalchemy_session = None  # workaround for a bug in factoryboy
        model = PerSectionAlignmentParameters

        sqlalchemy_get_or_create = ("id",)

    alignment = factory.SubFactory(
        AlignmentFactory,
    )
    z_index = fuzzy.FuzzyInteger(1, 1000)
    x_offset = fuzzy.FuzzyFloat(1, 100)
    y_offset = fuzzy.FuzzyFloat(1, 100)
    in_plane_rotation = fuzzy.FuzzyFloat(1, 100)
    beam_tilt = fuzzy.FuzzyFloat(1, 100)
    tilt_angle = fuzzy.FuzzyFloat(1, 100)
    id = fuzzy.FuzzyInteger(1, 1000)
