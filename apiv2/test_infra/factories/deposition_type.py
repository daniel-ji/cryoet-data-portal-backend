"""
Factory for generating DepositionType objects.

Auto-generated by running 'make codegen'. Do not edit.
Make changes to the template codegen/templates/test_infra/factories/class_name.py.j2 instead.
"""

# ruff: noqa: E501 Line too long

import random
import factory
import uuid6
from database.models import DepositionType
from platformics.test_infra.factories.base import FileFactory, CommonFactory
from test_infra.factories.deposition import DepositionFactory
from factory import Faker, fuzzy
from faker_biology.bioseq import Bioseq
from faker_biology.physiology import Organ
from faker_enum import EnumProvider

Faker.add_provider(Bioseq)
Faker.add_provider(Organ)
Faker.add_provider(EnumProvider)


class DepositionTypeFactory(CommonFactory):
    class Meta:
        sqlalchemy_session = None  # workaround for a bug in factoryboy
        model = DepositionType

        sqlalchemy_get_or_create = ("id",)

    deposition = factory.SubFactory(
        DepositionFactory,
    )
    type = fuzzy.FuzzyChoice(["annotation", "dataset", "tomogram"])
    id = fuzzy.FuzzyInteger(1, 1000)
