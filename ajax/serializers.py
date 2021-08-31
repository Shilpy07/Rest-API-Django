from ajax import models
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('name', 'email', 'gender', 'age')
