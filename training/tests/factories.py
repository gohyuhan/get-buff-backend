from factory.django import DjangoModelFactory

from training.models import (
    Exercise,
    PresetTrainingSet,
    PresetTrainingExercise,
    CustomTrainingSet,
    CustomTrainingExercise
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


class CustomTrainingSetFactory(DjangoModelFactory):
    class Meta:
        model = CustomTrainingSet


class CustomTrainingExerciseFactory(DjangoModelFactory):
    class Meta:
        model = CustomTrainingExercise