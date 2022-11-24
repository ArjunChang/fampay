from django.urls import path

from youtube.views import YouTubeVideoView

urlpatterns = [
    path('list', YouTubeVideoView.as_view(), name='list'),
]
