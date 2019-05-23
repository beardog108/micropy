from django.test import TestCase
from boards.models import PostDB, Boards

class PostTestCase(TestCase):
    def test_setUp(self):
        Boards.objects.create(board_name='meme')
        PostDB.objects.create(board_name='meme', content='hello world')

    