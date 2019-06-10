'''
    MicroPY - Textboard/forum written in Python
    Copyright (C) 2019 Kevin Froman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Boards
from micropy import settings
from boards import boardutils
from boards import forms
from . import postcreator

try:
    site_name = settings.SITE_NAME
except AttributeError:
    site_name = 'MicroPY'

STANDARD_CONTEXT = {
    'site_name': site_name,
    'board_list': boardutils.get_list_of_board_names()
}

def index(request):
    settings_to_load = ['SITE_MOTD', 'SITE_PRIVACY', 'SITE_RULES']
    context = {}
    for setting in settings_to_load:
        try:
            context[setting] = getattr(settings, setting)
        except AttributeError:
            print('darn', setting)
            pass

    context = dict({**STANDARD_CONTEXT, **context})
    template = loader.get_template('boards/index.html')
    resp = HttpResponse(template.render(context, request))
    return resp

def board_home(request, board_name):
    for board in STANDARD_CONTEXT['board_list']:
        if board_name == board.board_name:
            break
    else:
        raise Http404

    context = {'board_name': board_name, 'new_post_form': forms.NewPostForm, 'post_list': boardutils.get_post_list_for_board(board_name),}
    context = dict({**STANDARD_CONTEXT, **context})
    template = loader.get_template('boards/board-home.html')
    resp = HttpResponse(template.render(context, request))
    return resp

def submit_post(request):
    return postcreator.create_new_post(request)

def custom_admin(request):
    return HttpResponse("YEET")