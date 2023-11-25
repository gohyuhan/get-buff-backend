from factory.django import DjangoModelFactory

from training.models import (
    Exercise,
    PresetTrainingSet,
    PresetTrainingExercise
)


class ExerciseFactory(DjangoModelFactory):
    class Meta:
        model = Exercise


class PresetTrainingSetFactory(DjangoModelFactory):
    class Meta:
        model = PresetTrainingSet


class PresetTrainingExerciseFactory(DjangoModelFactory):
    class Meta:
        model = PresetTrainingExercise