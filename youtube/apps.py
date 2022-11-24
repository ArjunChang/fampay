from django.apps import AppConfig


class YoutubeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtube'

    def ready(self):
        """
        Start the task only after the models have been rendered
        :return:
        """
        from fampay.tasks import fetch_youtube_videos
        fetch_youtube_videos.delay()
