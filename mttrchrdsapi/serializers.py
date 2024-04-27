from rest_framework import serializers
from .models import Show, ShowCreator, ShowCategory, ShowPlatform, Game, GameCreator, GameCategory, GamePlatform, Activity
from django.conf import settings

class ShowPlatformSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = ShowPlatform
        fields = ['id', 'name', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.image.url
            return obj.image.url
        return ''

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
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ['id', 'name', 'creator', 'imdb_id', 'image_url', 'thumbnail_url', 'categories', 'rating']

    def get_image_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.image.url
            return obj.image.url
        return ''
    
    def get_thumbnail_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.thumbnail.url
            return obj.thumbnail.url
        return ''
    

class GamePlatformSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = GamePlatform
        fields = ['id', 'name', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.image.url
            return obj.image.url
        return ''

class GameCreatorSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = GameCreator
        fields = ['id', 'name', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.image.url
            return obj.image.url
        return ''


class GameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCategory
        fields = ['id', 'name']


class GameSerializer(serializers.ModelSerializer):
    creator = GameCreatorSerializer(read_only=True)
    categories = GameCategorySerializer(read_only=True, many=True)
    image_url = serializers.SerializerMethodField()
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'name', 'creator', 'imdb_id', 'image_url', 'thumbnail_url', 'categories', 'rating']

    def get_image_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.image.url
            return obj.image.url
        return ''
    
    def get_thumbnail_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.thumbnail.url
            return obj.thumbnail.url
        return ''
    

class ActivitySerializer(serializers.ModelSerializer):
    show_activity = ShowSerializer(read_only=True)
    show_platform = ShowPlatformSerializer(read_only=True)
    game_activity = GameSerializer(read_only=True)
    game_platform = GamePlatformSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'start_at', 'end_at', 'completed', 'show_activity', 'show_platform', 'game_activity', 'game_platform', 'activity_type']


class TimelineShowPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowPlatform
        fields = ['id', 'name']


class TimelineShowSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Show
        fields = ['id', 'name', 'thumbnail_url']
    
    def get_thumbnail_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.thumbnail.url
            return obj.thumbnail.url
        return ''


class TimelineGamePlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlatform
        fields = ['id', 'name']


class TimelineGameSerializer(serializers.ModelSerializer):
    thumbnail_url = serializers.SerializerMethodField()

    class Meta:
        model = Game
        fields = ['id', 'name', 'thumbnail_url']
    
    def get_thumbnail_url(self, obj):
        if obj.image:
            if settings.DEBUG:
                return settings.BASE_DOMAIN + obj.thumbnail.url
            return obj.thumbnail.url
        return ''


class TimelineActivitySerializer(serializers.ModelSerializer):
    show_activity = TimelineShowSerializer(read_only=True)
    show_platform = TimelineShowPlatformSerializer(read_only=True)
    game_activity = TimelineGameSerializer(read_only=True)
    game_platform = TimelineGamePlatformSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'start_at', 'end_at', 'completed', 'show_activity', 'show_platform', 'game_activity', 'game_platform', 'activity_type']


class TimelineSerializer(serializers.Serializer):
    date = serializers.DateField()
    day = serializers.CharField(max_length=100)
    month = serializers.CharField(max_length=100)
    year = serializers.CharField(max_length=100)
    channels = serializers.ListField(
        child=TimelineActivitySerializer(read_only=True)
    )


class StatsGameHoursSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    total = serializers.IntegerField()
