from django.urls import path, include
from watchlist_app.api.views import ReviewVeiwSet, WatchViewSet, StreamPlatformViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'review', ReviewVeiwSet)
router.register(r'watchlist', WatchViewSet)
router.register(r'stream', StreamPlatformViewSet)

urlpatterns = [
    path('', include(router.urls))
]
