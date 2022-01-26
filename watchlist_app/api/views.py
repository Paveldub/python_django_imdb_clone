# rest framework imports
from platform import platform
from re import T

# for mixins and generics
from rest_framework import mixins
from rest_framework import viewsets

# App imports
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# lists
# Concrete View Classes
class ReviewVeiwSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
        
class WatchViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

class StreamPlatformViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  viewsets.GenericViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    

    

    
        

        
        
        