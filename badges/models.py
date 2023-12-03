from datetime import datetime

from django.db import models

from enumfields import EnumField

from muscle.enums import MuscleGroup
from training.enums import (
    TrainingLevel,
    TrainingOrExerciseType
)
from .enums import (
    SpecialTargetType,
    TargetCountType,
)
from user.models import UserProfile

# Create your models here.

"""
NOTE: How Badges and its Model Work 

Badges in our system is a kind of rewards for earn through progression count.
there were two kind of badges: 
NOTE IMPORTANT: Never remove/delete both kind of Achivement Badges ( exception raise when delete() is called  )
1) SkeletonAchivementBadges - create as a base reference to be use during generation of UserAchivementBadges, 
                              also to keep track of what badges we have in our system 
2) UserAchivementBadges - An achivement badges tied to user to track the progression, obtained time and such

Other:
1) Track - a model to have info need to know what exactly does it track for
           e.g, it was tracking training for abs with begineer level and it was counting is using count ( others option like days/weeks)
2) badges - contain name and the image url for the badge
"""

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Track(BaseModel):
    """
    info to show what badges track to earn progress
    for count types of days,weeks,months and years, 
    they were means by 1 day, 1 week, 1 month and 1 year 
    NOTE: as what wwe plan for our system and what our app wanted to deliver, 
          we do not have a way to change that, meaning we can't have a way to track 2 days or 3 weeks
    """
    # these field are for non training types 
    special_target = EnumField(
        SpecialTargetType, 
        max_length=3,
        help_text=(
            f"[streak - to track about a continuous action]  "
            f"[none - default for non streak target]  "
        ),
        default = SpecialTargetType.NONE
    )

    # these fields are for training and exercise 
    type_target = EnumField(TrainingOrExerciseType, max_length=3)
    level_target = EnumField(TrainingLevel, max_length=3)
    muscle_target = EnumField(MuscleGroup, max_length=3)

    count_type = EnumField(TargetCountType, max_length=3)

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

    def delete(self, *args, **kwargs):
        # You can add your custom logic here to prevent deletion
        # For example, you can raise an exception
        raise Exception("Deletion of instances of this model is not allowed.")
    

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
    desp = models.TextField(
        help_text="Description about the badge and how to earn progress for it"
    )
    progress_count = models.PositiveIntegerField(default=0)
    obtain_time = models.DateTimeField(null=True, blank=True)
    is_obtained = models.BooleanField(default=False)
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
    
    def is_obtainable(self):
        return self.progress_count >= self.required_value
    
    def set_obtained(self):
        self.is_obtained = True
        self.obtain_time = datetime.now()
        self.save()

    def delete(self, *args, **kwargs):
        # You can add your custom logic here to prevent deletion
        # For example, you can raise an exception
        raise Exception("Deletion of instances of this model is not allowed.")
        