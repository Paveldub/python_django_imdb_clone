from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform

class WatchListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = WatchList
        fields = ['id', 'title', 'storyline', 'active', 'created']
        # '__all__'
        
class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = ['id', 'name',  'about', 'website']
