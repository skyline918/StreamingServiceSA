from django.contrib import admin

# Register your models here.
from core.models import *

admin.site.register(Video)
admin.site.register(VideoCategory)
admin.site.register(VideoStat)
admin.site.register(Comment)
admin.site.register(CDN)



