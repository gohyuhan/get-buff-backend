from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import (
    SkeletonAchivementBadge,
    UserAchivementBadge
)
from user.models import UserProfile


@receiver(pre_save, sender=SkeletonAchivementBadge)
def generate_newly_added_achivement_badges_for_user(sender, **kwargs):
    instance = kwargs.get('instance')

    if SkeletonAchivementBadge.objects.filter(id=instance.id).exists():
        old_instance = SkeletonAchivementBadge.objects.get(id=instance.id)
        UserAchivementBadge.objects.filter(
            desp = old_instance.desp,
            required_value = old_instance.required_value,
            badge = old_instance.badge,
            track =old_instance.track,
        ).update(
            desp = instance.desp,
            required_value = instance.required_value,
            badge = instance.badge,
            track =instance.track,
        )
    else:
        UserAchivementBadge.objects.bulk_create(
            [
                UserAchivementBadge(
                    user_profile = user_profile,
                    desp = instance.desp,
                    required_value = instance.required_value,
                    badge = instance.badge,
                    track =instance.track,
                )for user_profile in UserProfile.objects.all()
            ]
        )

