from rest_framework import serializers

from .models import UserAchivementBadge


class UserAchivementBadgeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source = "badge.name",max_length=512)
    image= serializers.URLField(source = "badge.image")
    class Meta:
        model = UserAchivementBadge
        fields = [
            'name',
            'desp',
            'image',
            'progress_count',
            'obtain_time',
            'is_obtained',
            'required_value'
        ]
