from django.shortcuts import render, HttpResponse

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Message
from .serializers import MessageSerializer

from rest_framework.exceptions import APIException

from datetime import datetime, timedelta
from django.utils import timezone

class MessageCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        last_hour_time = datetime.now(tz=timezone.utc) - timedelta(hours = 1)
        msg_in_last_hour = Message.objects.filter(created_by=request.user, created_at__gt = last_hour_time).count()
        
        if msg_in_last_hour >= 10:
            raise APIException("You can post maximum 10 post per hour")

        serializer = MessageSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)