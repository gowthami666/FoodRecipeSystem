from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user',UserViewSet)

urlpatterns = router.urls