from django.contrib import admin
from .models import Boards, PostDB, Site
# Register your models here.
admin.site.register(Boards)
admin.site.register(PostDB)
admin.site.register(Site)