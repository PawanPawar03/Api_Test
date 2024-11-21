from django.db import models
from django.contrib.auth.models import User


# user Model
class User(models.Model):
    User_name = models.CharField(max_length=255)
    user_lastname = models.CharField(max_length=255)
    user_mail = models.EmailField(max_length=255)
    user_phonenumber = models.IntegerField()

    def __str__(self):
        return self.User_name, self.user_lastname

# Client Model
class Client(models.Model):
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_name

# Project Model
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    users = models.ManyToManyField('auth.User', related_name="projects")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name
