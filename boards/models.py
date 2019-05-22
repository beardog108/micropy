from django.db import models

# Create your models here.

MAX_BOARD_NAME_LENGTH = 20

class Boards(models.Model):
    board_name = models.CharField(max_length=MAX_BOARD_NAME_LENGTH)
    password = models.TextField(blank=True)

    def __str__(self):
        return f'Board: {self.board_name}'

class Users:
    admin = models.BooleanField()
    board_permissions = models.TextField()

class PostDB(models.Model):
    board_name = models.TextField(max_length=MAX_BOARD_NAME_LENGTH)
    parent_id = models.IntegerField()
    tripcode = models.TextField(max_length=150)
    name = models.CharField(max_length=25)
    content = models.TextField(max_length=500000)