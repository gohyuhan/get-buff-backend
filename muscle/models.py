from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MuscleCategory(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Muscle(BaseModel):
    name = models.CharField(max_length=255)
    # image of muscle image from the front of a human body
    front_image_url = models.URLField()
    # image of muscle image from the back of a human body
    back_image_url = models.URLField()
    muscle_category = models.ForeignKey(
        MuscleCategory,
        blank=True,
        null = True,
        on_delete=models.PROTECT
    )
