from factory.django import DjangoModelFactory

from muscle.models import (
    Muscle,
    MuscleCategory
)


class MuscleFactory(DjangoModelFactory):
    class Meta:
        model = Muscle


class MuscleCategoryFactory(DjangoModelFactory):
    class Meta:
        model = MuscleCategory