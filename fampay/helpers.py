from youtube.models import Video


def process_youtube_response(results):
    """
    Use the response from youtube data api to fill the database
    :param results:
    :return: None
    """
    for result in results:
        snippet = result['snippet']
        Video.objects.get_or_create(
            video_id=result['id']['videoId'],
            title=snippet['title'],
            description=snippet['description'],
            channel=snippet['channelTitle'],
            published_at=snippet['publishTime'],
            thumbnail_url=snippet['thumbnails']['high']['url'],
        )
        print("Done Updating DB!")
