from ajax.models import *
from rest_framework import viewsets
from ajax import serializers

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
    filterset_fields = ('name',)
    extra_kwargs = {'url': {'lookup_field': 'name'}}