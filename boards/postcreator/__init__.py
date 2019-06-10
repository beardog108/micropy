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
import time, math
from django.shortcuts import redirect
from django.http import HttpResponse
from boards import models

def create_new_post(request):
    posted_board = request.POST['board_name']
    new_post = models.PostDB(board_name=posted_board, title=request.POST['post_title'], content=request.POST['post_content'], date=math.floor(time.time()))
    new_post.save()
    return redirect('/%s/' % (posted_board,))
    #return HttpResponse("Success, posted %s with id %s" % (request.POST['post_title'], new_post.id))