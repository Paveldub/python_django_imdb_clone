from django.urls import path, include
from watchlist_app.api.views import ReviewVeiwSet, WatchViewSet, StreamPlatformViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'review', ReviewVeiwSet)
router.register(r'watchview', WatchViewSet)
router.register(r'stream-platform', StreamPlatformViewSet)

urlpatterns = [
    path('', include(router.urls))
]
