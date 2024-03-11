from .models import Show, ShowCreator, ShowPlatform, ShowCategory, Game, GameCreator, GamePlatform, GameCategory, Activity

from .serializers import ShowSerializer, ShowCreatorSerializer, ShowPlatformSerializer, ShowCategorySerializer, GameSerializer, GameCreatorSerializer, GamePlatformSerializer, GameCategorySerializer, ActivitySerializer, TimelineSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import date, timedelta, datetime

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

@api_view(['GET'])
def timeline_ongoing(request):
    activities = Activity.objects.filter(end_at=None)
    serializer = TimelineSerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def timeline(request):
    start_param = request.query_params.get('start', None)
    end_param = request.query_params.get('end', None)
    channels_param = request.query_params.get('channels', None)

    start_date = datetime.strptime(start_param, '%Y-%m-%d').date()
    end_date = datetime.strptime(end_param, '%Y-%m-%d').date()

    first_activity = Activity.objects.order_by('start_at').first()

    def daterange(start, end):
        for n in range(int((end - start).days) + 1):
            yield end - timedelta(n)

    channels = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
    ]

    # if an existing channel list is active and passed as an argument, start channels from that point
    if channels_param:
        tmpChannels = []
        existing_channels = channels_param.split(',')
        for c in existing_channels:
            #TODO refactor this to try/catch
            if c:
                tmpChannels.append(Activity.objects.get(id=c))
            else:
                tmpChannels.append(None)
        channels = tmpChannels

    timeline_days = []

    for timeline_day in daterange(start_date, end_date):
        # Prevents returning data beyond first ever activity
        if (timeline_day >= first_activity.start_at):
            # Clear channels when we are past their activities start date
            channel_indexes = []
            for idx, channel in enumerate(channels):
                if channel:
                    if channel.start_at == timeline_day + timedelta(1):
                        channel_indexes.append(idx)
            for channel_index in channel_indexes:
                channels[channel_index] = None

            # Assign today's activities to channels
            if timeline_day == date.today():
                today_activities = Activity.objects.filter(end_at=None)
            else:
                today_activities = Activity.objects.filter(end_at=timeline_day)

            for today_activity in today_activities:
                channel_index = channels.index(None)
                channels[channel_index] = today_activity

            timeline_days.append({
                'date': timeline_day,
                'day': timeline_day.strftime('%d'),
                'month': timeline_day.strftime('%m'),
                'year': timeline_day.strftime('%Y'),
                'channels': [
                    channels[0],
                    channels[1],
                    channels[2],
                    channels[3],
                    channels[4],
                    channels[5],
                    channels[6],
                ],
            })

    serializer = TimelineSerializer(timeline_days, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def latest_shows(request):
    latest_activities = Activity.objects.filter(show_activity__isnull=False).order_by('-end_at')[:3]
    serializer = ActivitySerializer(latest_activities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def latest_games(request):
    latest_activities = Activity.objects.filter(game_activity__isnull=False).order_by('-end_at')[:3]
    serializer = ActivitySerializer(latest_activities, many=True)
    return Response(serializer.data)