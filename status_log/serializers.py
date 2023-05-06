from rest_framework import serializers
from status_log import models

class StatusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatusLog
        fields = ('id', 'user_id', 'log_message', 'created_on')
        extra_kwargs = {'user_id': {'read_only': True}}
