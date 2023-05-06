from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


from status_log import serializers
from status_log import models
# Create your views here.

class StatusLogViewSet(viewsets.ModelViewSet):
    queryset = models.StatusLog.objects.all()
    serializer_class = serializers.StatusLogSerializer
    authentication_classes = (TokenAuthentication,)


    def perform_create(self, serializer):
        """set the profile to the logged in user"""
        serializer.save(user_id=self.request.user)
