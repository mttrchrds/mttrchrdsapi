from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date, timedelta, datetime
import calendar

from .models import Show, ShowCreator, ShowPlatform, ShowCategory, Game, GameCreator, GamePlatform, GameCategory, Activity
from .serializers import ShowSerializer, ShowCreatorSerializer, ShowPlatformSerializer, ShowCategorySerializer, GameSerializer, GameCreatorSerializer, GamePlatformSerializer, GameCategorySerializer, ActivitySerializer, TimelineSerializer, StatsGameHoursSerializer, StatsShowPlatformsYearsSerializer, StatsGameCategoriesSerializer, StatsActivityMonthsSerializer

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
    channels_param = request.query_params.get('channels', [])

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
    if len(channels_param) > 0:
        tmp_channels = []
        existing_channels = channels_param.split(',')
        for c in existing_channels:
            if c:
                try:
                    tmp_channels.append(Activity.objects.get(id=c))
                except Activity.DoesNotExist:
                    tmp_channels.append(None)
            else:
                tmp_channels.append(None)   
        channels = tmp_channels

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


@api_view(['GET'])
def stats_game_days(request):
    limit_param = request.query_params.get('limit', 10)
    game_activities = Activity.objects.filter(game_activity__isnull=False, end_at__isnull=False)
    games = {}
    stats = []
    for activity in game_activities:
        game_id = activity.game_activity.id
        total_days = (activity.end_at - activity.start_at).days
        if game_id in games:
            games[game_id]['total_days'] = games[game_id]['total_days'] + total_days
        else:
            games[game_id] = {
                'name': activity.game_activity.name,
                'total_days': total_days,
            }
    for game_id in games.keys():
        stats.append({
            'id': game_id,
            'name': games[game_id]['name'],
            'total': games[game_id]['total_days'],
        })
    stats.sort(key=lambda x: x['total'], reverse=True)
    serializer = StatsGameHoursSerializer(stats[:int(limit_param)], many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stats_show_platforms_years(request):
    show_platforms = ShowPlatform.objects.all().exclude(name__in=["Warhammer TV","ITV X","Channel 4","Blu-ray"])
    years = ['2021','2022','2023','2024']
    highest_value = 0
    stats = []
    for platform in show_platforms:
        item = {
            'platform': platform.name,
            'years': [],
        }
        for year in years:
            start_date = year + '-01-01'
            end_date = year + '-12-31'
            total = Activity.objects.filter(show_activity__isnull=False, end_at__isnull=False, start_at__gte=start_date, start_at__lte=end_date, show_platform=platform).count()
            if total > highest_value:
                highest_value = total
            item['years'].append({
                'name': year,
                'total': total,
            })
        stats.append(item)
    payload = {
        'years': years,
        'highest': highest_value,
        'data': stats,
    }
    serializer = StatsShowPlatformsYearsSerializer(payload)
    return Response(serializer.data)


@api_view(['GET'])
def stats_game_categories(request):
    game_activities = Activity.objects.filter(game_activity__isnull=False, end_at__isnull=False)
    categories_stats = {}
    unique_games = {}
    stats_parsed = []
    for activity in game_activities:
        game_id = activity.game_activity.id
        if not game_id in unique_games:
            unique_games[game_id] = activity.game_activity.categories
    for game_id in unique_games.keys():
        for cat in unique_games[game_id].all():
            if cat.id in categories_stats:
                categories_stats[cat.id]['total'] = categories_stats[cat.id]['total'] + 1
            else:
                categories_stats[cat.id] = {
                    'name': cat.name,
                    'total': 1
                }
    for category_id in categories_stats.keys():
        stats_parsed.append({
            'id': category_id,
            'name': categories_stats[category_id]['name'],
            'total': categories_stats[category_id]['total'],
        })
    serializer = StatsGameCategoriesSerializer(stats_parsed, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def stats_activity_months(request):
    years = ['2021','2022','2023','2024']
    data = []
    for month_idx in range(1, 13):
        payload = {
            'name': calendar.month_abbr[month_idx],
            'years': []
        }
        for year in years:
            month_range = calendar.monthrange(int(year), month_idx)
            two_digit_month = f"{month_idx:02d}"
            month_end_day = month_range[1]
            two_digit_month_end_day = f"{month_end_day:02d}"
            end_of_month = year + '-' + two_digit_month + '-' + two_digit_month_end_day
            start_of_month = year + '-' + two_digit_month + '-01'
            monthly_activity_total = Activity.objects.filter(start_at__lte=end_of_month, end_at__gte=start_of_month).count()
            year_payload = {
                'name': year,
                'total': monthly_activity_total
            }
            payload['years'].append(year_payload)
        data.append(payload)

    serializer = StatsActivityMonthsSerializer(data, many=True)
    return Response(serializer.data)
