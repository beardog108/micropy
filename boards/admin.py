from django.contrib import admin
from .models import Boards, PostDB
from micropy import settings

try:
    site_name = settings.SITE_NAME
except AttributeError:
    site_name = 'MicroPY'
site_name += ' Admin'

# Register your models here.

admin.site.register(Boards)
admin.site.register(PostDB)

admin.site.site_header = site_name