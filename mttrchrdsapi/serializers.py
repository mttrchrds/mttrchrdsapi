from rest_framework import serializers
from .models import Show, ShowCreator, ShowCategory
from django.conf import settings

class ShowCreatorSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ShowCreator
        fields = ['id', 'name', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.image.url
            return obj.image.url
        return ''


class ShowCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowCategory
        fields = ['id', 'name']


class ShowSerializer(serializers.ModelSerializer):
    creator = ShowCreatorSerializer(read_only=True)
    categories = ShowCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Show
        fields = ['id', 'name', 'creator', 'imdb_id', 'image', 'categories']