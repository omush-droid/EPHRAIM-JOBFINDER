from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet, NotificationViewSet

router = DefaultRouter()
router.register(r'follows', FollowViewSet, basename='follow')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]