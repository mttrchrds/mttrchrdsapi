from rest_framework import serializers
from .models import Show, ShowCreator, ShowCategory

class ShowCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowCreator
        fields = ['id', 'name', 'image_url']


class ShowCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowCategory
        fields = ['id', 'name']


class ShowSerializer(serializers.ModelSerializer):
    creator = ShowCreatorSerializer(read_only=True)
    categories = ShowCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Show
        fields = ['id', 'name', 'creator', 'imdb_id', 'image_url', 'categories']