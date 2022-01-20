from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = WatchList
        fields = ('id', 'title', 'storyline', 'active', 'created')
        # fields = '__all__'
        # better to use tupple ()

        
class StreamPlatformSerializer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='watch_details'
    )
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # fields = ('id', 'name', 'about', 'website')
