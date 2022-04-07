from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from todo.models import Todo


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    user = request.user
    dates = user.tasks.all().values_list("date",flat=True).distinct()
    
    data = {str(date): user.tasks.filter(date=date).values() for date in dates} 
    
    return Response(data, status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def productivity_stats(request):
    user = request.user
    
    data = {"pending": user.tasks.filter(status="pending").count(),
            "completed": user.tasks.filter(status="completed").count()}
    
    return Response(data, status=status.HTTP_200_OK)
    