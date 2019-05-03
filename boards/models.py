from django.db import models

# Create your models here.

class Boards(models.Model):
    board_name = models.CharField(max_length=120)
    password = models.TextField(blank=True)

class Users:
    admin = models.BooleanField()
    board_permissions = models.TextField()

class PostDB(models.Model):
    parent_id = models.IntegerField
    tripcode = models.TextField(max_length=150)
    name = models.CharField(max_length=25)
    content = models.TextField(max_length=500000)