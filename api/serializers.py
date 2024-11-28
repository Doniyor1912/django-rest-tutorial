from rest_framework import serializers

from api.models import Container


class SerializerPerson(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = "__all__"