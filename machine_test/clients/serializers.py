from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

# User Serializer (optional if you want to list user details in the project)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Client Serializer
class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    projects = serializers.StringRelatedField(many=True)
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'projects']

    def get_projects(self, obj):
        return [{'id': project.id, 'name': project.project_name} for project in obj.projects.all()]

# Project Serializer
class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name')
    users = UserSerializer(many=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client_name', 'users', 'created_at', 'created_by']