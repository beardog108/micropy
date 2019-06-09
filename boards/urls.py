from django.urls import path, include

from . import views, boardutils

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-post', views.submit_post, name='submit_post'),
    path('<str:board_name>/', views.board_home, name="board_name")
]