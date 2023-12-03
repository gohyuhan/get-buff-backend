from django.contrib import admin


from .models import (
    Track,
    Badge,
    SkeletonAchivementBadge,
    UserAchivementBadge
)


# Register your models here.
admin.site.register(Track)
admin.site.register(Badge)
admin.site.register(SkeletonAchivementBadge)
admin.site.register(UserAchivementBadge)