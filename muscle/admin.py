from django.contrib import admin

from muscle.models import(
    Muscle,
    MuscleCategory
)


# Register your models here.
admin.site.register(Muscle)
admin.site.register(MuscleCategory)