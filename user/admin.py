from django.contrib import admin

from user.models import (
    UserProfile,
    TrainingSetCompletedRecord,
    TrainingSetting
)


# Register your models here.
admin.site.register(UserProfile)
admin.site.register(TrainingSetCompletedRecord)
admin.site.register(TrainingSetting)
