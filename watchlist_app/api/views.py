# DEFAULT PERMISSIONS
from rest_framework.permissions import IsAuthenticated

# for mixins and generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response

# App imports
from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.pagination import WatchListPagination
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

# CUSTOM PERMISSIONS 
from watchlist_app.api.permissions import ReviewUserOrReadOnly

# lists
# Concrete View Classes

# DJANGO Filter library
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class UserReview(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_user__username', 'active']
    
    def queryset_set(self):
        username = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=username)
    
class ReviewViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer
    # if user auth show this data
    # permission_classes = [IsAuthenticated]
    
    def list(self, request):
        print(request.user)
        queryset = Review.objects.filter()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)

class WatchList(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer
    pagination_class = WatchListPagination
    # search filter
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^title', '=platform__name']
    
    # filter backend
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'platform__name']
    
    # order filters
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'platform__name']
    
    
# class WatchViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    # queryset = WatchList.objects.all()
    # serializer_class = WatchListSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]
   
class StreamPlatformViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,  viewsets.GenericViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    

    

    
        

        
        
        