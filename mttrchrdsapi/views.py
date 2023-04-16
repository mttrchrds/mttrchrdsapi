from .models import Show, ShowCreator, ShowPlatform, ShowCategory, Game, GameCreator, GamePlatform, GameCategory, Activity
from .serializers import ShowSerializer, ShowCreatorSerializer, ShowPlatformSerializer, ShowCategorySerializer, GameSerializer, GameCreatorSerializer, GamePlatformSerializer, GameCategorySerializer, ActivitySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def show_list(request):
    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_detail(request, id):
    try:
       show = Show.objects.get(pk=id)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ShowSerializer(show)
    return Response(serializer.data)

@api_view(['GET'])
def show_creator_list(request):
    show_creators = ShowCreator.objects.all()
    serializer = ShowCreatorSerializer(show_creators, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_creator_detail(request, id):
    try:
       show_creator = ShowCreator.objects.get(pk=id)
    except ShowCreator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ShowCreatorSerializer(show_creator)
    return Response(serializer.data)

@api_view(['GET'])
def show_platform_list(request):
    show_platforms = ShowPlatform.objects.all()
    serializer = ShowPlatformSerializer(show_platforms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_platform_detail(request, id):
    try:
       show_platform = ShowPlatform.objects.get(pk=id)
    except ShowPlatform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ShowPlatformSerializer(show_platform)
    return Response(serializer.data)

@api_view(['GET'])
def show_category_list(request):
    show_categories = ShowCategory.objects.all()
    serializer = ShowCategorySerializer(show_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def show_category_detail(request, id):
    try:
       show_category = ShowCategory.objects.get(pk=id)
    except ShowCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ShowCategorySerializer(show_category)
    return Response(serializer.data)

@api_view(['GET'])
def game_list(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def game_detail(request, id):
    try:
       game = Game.objects.get(pk=id)
    except Game.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GameSerializer(game)
    return Response(serializer.data)

@api_view(['GET'])
def game_creator_list(request):
    game_creators = GameCreator.objects.all()
    serializer = GameCreatorSerializer(game_creators, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def game_creator_detail(request, id):
    try:
       game_creator = GameCreator.objects.get(pk=id)
    except GameCreator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GameCreatorSerializer(game_creator)
    return Response(serializer.data)

@api_view(['GET'])
def game_platform_list(request):
    game_platforms = GamePlatform.objects.all()
    serializer = GamePlatformSerializer(game_platforms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def game_platform_detail(request, id):
    try:
       game_platform = GamePlatform.objects.get(pk=id)
    except GamePlatform.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GamePlatformSerializer(game_platform)
    return Response(serializer.data)

@api_view(['GET'])
def game_category_list(request):
    game_categories = GameCategory.objects.all()
    serializer = GameCategorySerializer(game_categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def game_category_detail(request, id):
    try:
       game_category = GameCategory.objects.get(pk=id)
    except GameCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = GameCategorySerializer(game_category)
    return Response(serializer.data)

@api_view(['GET'])
def activity_list(request):
    activites = Activity.objects.all()
    serializer = ActivitySerializer(activites, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def activity_detail(request, id):
    try:
       activity = Activity.objects.get(pk=id)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = ActivitySerializer(activity)
    return Response(serializer.data)
