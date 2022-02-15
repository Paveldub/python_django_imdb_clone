from django.urls import path, include
from watchlist_app.api.views import ReviewViewSet, StreamPlatformViewSet, UserReview, WatchList
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'review', ReviewViewSet)
# router.register(r'watchlist', WatchViewSet)
router.register(r'stream', StreamPlatformViewSet)
router.register(r'user-review', UserReview)
router.register(r'list2', WatchList)

urlpatterns = [
    path('', include(router.urls))
]
