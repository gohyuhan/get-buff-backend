from django.db import models

from enumfields import EnumField

from muscle.enums import MuscleGroup
from training.enums import (
    TrainingLevel,
    TrainingOrExerciseType
)
from .enums import (
    SpecialTargetType,
    SpecialTargetCountType
)
from user.models import UserProfile

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Track(BaseModel):
    """
    info to show what badges track to earn progress
    """
    # these field are for non training types 
    special_target = EnumField(SpecialTargetType, max_length=3)
    count_type = EnumField(SpecialTargetCountType, max_length=3)

    # these fields are for training and exercise 
    type_target = EnumField(TrainingOrExerciseType, max_length=3)
    level_target = EnumField(TrainingLevel, max_length=3)
    muscle_target = EnumField(MuscleGroup, max_length=3)

    def __str__(self):
        return f"{self.special_target} : {self.count_type} : {self.type_target} : {self.level_target} : {self.muscle_target}"


class Badge(BaseModel):
    """
    The base info for badges that we have in the system.
    """
    name = models.CharField(max_length=512)
    image = models.URLField()

    def __str__(self):
        return self.name


class SkeletonAchivementBadge(BaseModel):
    """
    base info for achivement badges like what are the badges and what it tracks to earn progression
    """
    desp = models.TextField(
        help_text="Description about the badge and how to earn progress for it"
    )
    required_value = models.PositiveIntegerField(
        help_text="Description about the progression count needed to obtain the achivement badge"
    )
    badge = models.ForeignKey(
        Badge,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    track = models.ForeignKey(
        Track,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.badge.name} - {self.track}"
    

class UserAchivementBadge(BaseModel):
    """
    base info for achivement badges like what are the badges and what it tracks to earn progression
    """
    user_profile = models.ForeignKey(
        UserProfile,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    progress_count = models.PositiveIntegerField(default=0)
    obtain_time = models.DateTimeField()
    is_obtained = models.BooleanField(default=False)
    desp = models.TextField(
        help_text="Description about the badge and how to earn progress for it"
    )
    required_value = models.PositiveIntegerField(
        help_text="Description about the progression count needed to obtain the achivement badge"
    )
    badge = models.ForeignKey(
        Badge,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )
    track = models.ForeignKey(
        Track,
        null=False,
        blank=False,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"{self.user_profile} - {self.badge.name}"