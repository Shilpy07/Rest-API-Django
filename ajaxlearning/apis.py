from rest_framework import routers
from ajax import api_views

router = routers.DefaultRouter()
router.register(r'Profile', api_views.ProfileViewset)