from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Client, Project, User
from .serializers import ClientSerializer, ProjectSerializer, UserSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Client ViewSet
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Project ViewSet
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client = Client.objects.get(id=self.request.data.get('client_id'))
        serializer.save(client=client, created_by=self.request.user)

    @action(detail=False, methods=['get'])
    def assigned_to_me(self, request):
        user = request.user
        projects = Project.objects.filter(users=request.user)
        serializer = self.get_serializer(projects, many=True)
        return Response(serializer.data)
