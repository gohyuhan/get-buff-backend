from django.db import models

from enumfields import EnumField

from user.models import UserProfile
from muscle.models import Muscle, MuscleCategory
from training.enums import (
    TrainingLevel, 
    CalculatedIn, 
    TrainingStatus, 
    TrainingType
)


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Exercise(BaseModel):
    """
    Info for all exercise we provided
    """
    name = models.CharField(max_length=255)
    explanation = models.TextField()
    calculate_in = EnumField(CalculatedIn, max_length=3)
    animation = models.URLField()
    muscle = models.ManyToManyField(
        Muscle,
        help_text="to show what muscles were involve in this exercise, could be more than 1"
    )
    muscle_category = models.ManyToManyField(
        MuscleCategory,
        help_text="to show what muscle categories is this excercise belong to, could be more than 1"
    )
    min_count = models.PositiveIntegerField(
        help_text="minimum number of reps or seconds need to init for this exercise",
        default=0
    )

    def __str__(self):
        self.name


class PresetTrainingSet(BaseModel):
    """
    Info for a Training Set Premade available 
    """
    name = models.CharField(max_length=255)
    level = EnumField(TrainingLevel, max_length=3)
    muscle_category = models.ForeignKey(
        MuscleCategory,
        blank=True, 
        null=True,
        on_delete=models.PROTECT
    )

    @property
    def preset_training_exercise(self):
        return PresetTrainingExercise.objects.filter(belong_to_training_set=self).order_by("order")

    def __str__(self):
        return f"{self.name} - {self.level}"
    

class PresetTrainingExercise(BaseModel):
    """
    Info for a Training Exercise Premade available that link with a Premade Training Set
    """
    calculate_in = EnumField(CalculatedIn, max_length=3)
    required_value = models.PositiveIntegerField()
    level = EnumField(TrainingLevel, max_length=3)
    belong_to_training_set = models.ForeignKey(
        PresetTrainingSet,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    exercise = models.ForeignKey(
        Exercise,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    order=models.PositiveIntegerField(
        help_text="to show the order of each exersice in a training set"
    )

    def __str__(self):
        return f"{self.exercise.name} - {self.level} - belong to: {self.belong_to_training_set.name}"

    
class CustomTrainingSet(BaseModel):
    """
    Info/Record of training set for users
    """
    user_profile = models.ForeignKey(
        UserProfile,
        blank=False,
        null=False,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    level = EnumField(
        TrainingLevel, 
        default=None, 
        null=True, 
        blank=True,
        max_length = 3
    )
    muscle_category = models.ForeignKey(
        MuscleCategory,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    status = EnumField(
        TrainingStatus, 
        max_length=3,
        default=TrainingStatus.ONGOING
    )
    training_type = EnumField(
        TrainingType,
        max_length=3,
        help_text = "to indicate if this training set is created base on our preset Training set or user custom training set"
    )

    @property
    def custom_preset_training_exercise(self):
        return CustomTrainingExercise.objects.filter(belong_to_custom_training_set=self).order_by("order")

    def __str__(self):
        return (
            f"{self.user_profile.user.first_name} {self.user_profile.user.last_name} - {self.name} - {self.type} - {self.status}"
        )
    

class CustomTrainingExercise(BaseModel):
    """
    Info/Record of training exercise for users
    """
    calculate_in = EnumField(CalculatedIn, max_length=3)
    required_value = models.PositiveIntegerField()
    level = EnumField(TrainingLevel, max_length=3)
    belong_to_custom_training_set = models.ForeignKey(
        CustomTrainingSet,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        Exercise,
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    order = models.PositiveIntegerField(
        help_text="to show the order of each exersice in a training set"
    )
    status = EnumField(
        TrainingStatus,
        max_length=3,
        default=TrainingStatus.ONGOING
    )

    def __str__(self):
        return f"{self.exercise.name} - {self.status}"

