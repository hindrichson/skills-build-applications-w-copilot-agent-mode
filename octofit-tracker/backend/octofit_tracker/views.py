from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    base_url = "https://curly-computing-machine-5jr67xrjww634vpg-8000.app.github.dev"
    codespace_suffix = ''  # Adding codespace suffix
    return Response({
        'users': f'{base_url}{codespace_suffix}/api/users/',
        'teams': f'{base_url}{codespace_suffix}/api/teams/',
        'activities': f'{base_url}{codespace_suffix}/api/activities/',
        'leaderboard': f'{base_url}{codespace_suffix}/api/leaderboard/',
        'workouts': f'{base_url}{codespace_suffix}/api/workouts/'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer