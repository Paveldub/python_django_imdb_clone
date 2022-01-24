from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        # fields = ('id', 'rating', 'description', 'created', 'update', 'active')
    
class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
   
    class Meta:
        model = WatchList
        # fields = ('id', 'title', 'storyline', 'active', 'created')
        fields = '__all__'

        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # fields = ('id', 'name', 'about', 'website')

