from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='watch_details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream')
]
