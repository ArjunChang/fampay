from django.contrib import admin
from youtube.models import Video, YouTubeAPIKey


class VideoAdmin(admin.ModelAdmin):
    pass


class YouTubeAPIKeyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)
admin.site.register(YouTubeAPIKey, YouTubeAPIKeyAdmin)
