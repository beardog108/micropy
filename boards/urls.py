from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('boards/<str:board_name>/', views.board_home, name='board_home')
]
