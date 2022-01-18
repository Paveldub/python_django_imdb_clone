from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ['id', 'name', 'description', 'active']
        # exclude = ['active']
        # '__all__'
        
    # object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError('Title and description should be different')
        else:
            return data
        
    # separate field validation (name)
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value
