from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializer import UserAchivementBadgeSerializer
from .models import UserAchivementBadge
# Create your views here.


class UserAchivementBadgeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        badges = UserAchivementBadge.objects.filter(user_profile__user=user).order_by('id')
        serializer = UserAchivementBadgeSerializer(badges, many=True)
        return Response({'success':True, 'data':serializer.data},status=status.HTTP_200_OK )
