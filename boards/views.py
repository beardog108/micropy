from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Boards

def index(request):
    output = ''
    for x in Boards.objects.all():
        output += x.board_name
        output += ','
    output = output[:-1]
    return HttpResponse(output)