from .models import (
    Track,
    Badge,
    SkeletonAchivementBadge,
    UserAchivementBadge
)


# services
"""
NOTE: the achivement badges currently are only planned to be tracking training/exercise by counts,
      for special, it will also be tracking training streak by day counts.

NOTE IMPORTANT: be sure to be clear about how we track and handle achivement badges before working on it>
                ESPECIALLY about tracking
"""

def user_achivement_badge_create(user_profile):
    """
    a services to generate achivement badges for individual user,
    for more detail about badges work see `badges.model`
    """
    existing_user_badges_id = [
        badge.id for badge in
        UserAchivementBadge.objects.select_related('badge').filter(user_profile=user_profile)
    ] 

    # here the unown_badges didn't mean unobtained but didn't create for user to be tracked
    user_unown_badges = [
        SkeletonAchivementBadge.objects.all().exclude(badge__id__in=existing_user_badges_id)
    ]

    UserAchivementBadge.objects.bulk_create(
        [
            UserAchivementBadge(
                user_profile = user_profile,
                desp = badge.desp,
                required_value = badge.required_value,
                badge = badge.badge,
                track = badge.track
            )for badge in user_unown_badges
        ]
    )


def user_training_achivement_badge_progression_update(user_profile):
    """
    a services to update non special training/exercise tracked achivement badges
    """
    pass
 

def user_training_streak_achivement_badge_progression_update(user_profile):
    """
    a services to update special (streak) training/exercise tracked achivement badges
    """
    pass