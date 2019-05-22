from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Boards
from micropy import settings
from boards import boardutils

try:
    site_name = settings.SITE_NAME
except AttributeError:
    site_name = 'MicroPY'

STANDARD_CONTEXT = {
    'site_name': site_name,
    'board_list': boardutils.get_list_of_board_names()
}

def index(request):
    template = loader.get_template('boards/index.html')
    resp = HttpResponse(template.render(STANDARD_CONTEXT, request))
    resp['access-control-allow-origin'] = '*'
    return resp

def board_home(request, board_name):
    context = {'board_name': board_name}
    context = dict({**STANDARD_CONTEXT, **context})
    template = loader.get_template('boards/board-home.html')
    resp = HttpResponse(template.render(context, request))
    return resp