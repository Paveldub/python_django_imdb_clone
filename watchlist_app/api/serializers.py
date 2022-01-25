from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'rating', 'description', 'created', 'update', 'active', 'watchlist')
    
class WatchListSerializer(serializers.ModelSerializer):
    # add reviews in fields
    reviews = ReviewSerializer(many=True, read_only=True)
   
    class Meta:
        model = WatchList
        fields = ('id', 'title', 'storyline', 'active', 'created', 'reviews')

        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = ('id', 'name', 'about', 'website', 'watchlist')

