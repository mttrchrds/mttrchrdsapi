from .models import Show
from .serializers import ShowSerializer
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
