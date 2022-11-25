import logging
import os

from celery import shared_task
from django.db import ProgrammingError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from fampay.helpers import process_youtube_response
from youtube.models import YouTubeAPIKey


@shared_task()
def fetch_youtube_videos():
    # Use multiple api keys to overcome quota exceeded error
    try:
        api_keys = YouTubeAPIKey.objects.values_list('api_key', flat=True)
    except ProgrammingError:
        logging.info("No API Key in DB.")
        api_keys = [os.environ.get('DEFAULT_YOUTUBE_API_KEY'), ]

    for api_key in api_keys:
        try:
            youtube = build('youtube', 'v3', developerKey=api_key)
            while True:
                search_response = youtube.search().list(
                    q='cats',
                    type='video',
                    order='date',
                    part='id,snippet',
                    maxResults=10,
                    publishedAfter="2022-01-01T00:00:00.000+00:00"
                ).execute()
                results = search_response['items']
                process_youtube_response(results)

        except HttpError as E:
            logging.error("HTTP Error: Check API Key and Quota")
            continue
