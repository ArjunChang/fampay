from time import sleep

from celery import shared_task
from googleapiclient.discovery import build

from fampay.helpers import process_youtube_response

KEY = 'AIzaSyD047QAtGwkA7mcShbSs2ExJw7a42gFHGY'


@shared_task()
def fetch_youtube_videos():
    youtube = build('youtube', 'v3', developerKey=KEY)
    while True:
        search_response = youtube.search().list(
            q='cats',
            type='video',
            part='id,snippet',
            maxResults=5
        ).execute()
        results = search_response['items']
        process_youtube_response(results)

        sleep(120)

