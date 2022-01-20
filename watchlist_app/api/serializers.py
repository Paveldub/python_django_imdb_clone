from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = WatchList
        fields = ('id', 'title', 'storyline', 'active', 'created')
        # better to use tupple ()

        
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        # better to use tupple ()
     