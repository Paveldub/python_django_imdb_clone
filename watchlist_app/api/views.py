# rest framework imports
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# for mixins and generics
from rest_framework import mixins
from rest_framework import viewsets

# App imports
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# PERMISSIONS 
from watchlist_app.api.permissions import AdminOrReadOnly

# lists
# Concrete View Classes
class ReviewVeiwSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    # if user auth show this data
    permission_classes = [AdminOrReadOnly]
        
class WatchViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
     # if user auth show this data
    permission_classes = [IsAuthenticated]

class StreamPlatformViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  viewsets.GenericViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    

    

    
        

        
        
        