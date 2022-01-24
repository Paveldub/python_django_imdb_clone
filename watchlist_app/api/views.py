# rest framework imports
from platform import platform
from re import T
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# for mixins and generics
from rest_framework import generics
from rest_framework import mixins

# App imports
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# lists

# Concrete View Classes
class ReviewList(generics.ListCreateAPIView):    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class WatchListAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StreamPlatformAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):  
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   
    
# details (each item)
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    
class StreamPlatformDetailAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):  
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, pk):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, pk):
        return self.destroy(request, *args, **kwargs)
    
class WatchDetailAV(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, pk):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, pk):
        return self.destroy(request, *args, **kwargs)
    
        

        
        
        