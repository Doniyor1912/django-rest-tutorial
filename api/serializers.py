from rest_framework import serializers

from api.models import Container


class SerializerPerson(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault)
    class Meta:
        model = Container
        fields = "__all__"