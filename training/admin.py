from django.contrib import admin

from training.models import (
    Exercise,
    PresetTrainingExercise,
    PresetTrainingSet,
    CustomTrainingExercise,
    CustomTrainingSet
)


# Register your models here.
admin.site.register(Exercise)
admin.site.register(PresetTrainingExercise)
admin.site.register(PresetTrainingSet)
admin.site.register(CustomTrainingExercise)
admin.site.register(CustomTrainingSet)
