from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetails
from rest_framework import routers

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='platform_details'),
    path('review/', ReviewList.as_view(), name='stream_detail'),
    path('review/<int:pk>', ReviewDetails.as_view(), name='review_detail'),
]
