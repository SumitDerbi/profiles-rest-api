from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serialises a name field for the testing our apiview """
    name = serializers.CharField(max_length=10)
