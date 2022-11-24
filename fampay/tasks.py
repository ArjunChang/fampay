from time import sleep

from celery import shared_task
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from fampay.helpers import process_youtube_response
from youtube.models import YouTubeAPIKey


@shared_task()
def fetch_youtube_videos():
    api_keys = YouTubeAPIKey.objects.all()
    for api_key in api_keys:
        try:
            youtube = build('youtube', 'v3', developerKey=api_key.api_key)
            while True:
                search_response = youtube.search().list(
                    q='cats',
                    type='video',
                    order='date',
                    part='id,snippet',
                    maxResults=5,
                    publishedAfter="2022-01-01T00:00:00.000+00:00"
                ).execute()
                results = search_response['items']
                process_youtube_response(results)

                sleep(120)

        except HttpError:
            continue
