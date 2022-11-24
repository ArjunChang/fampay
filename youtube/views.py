from django.views.generic import ListView

from youtube.models import Video


class YouTubeVideoView(ListView):
    model = Video
    paginate_by = 5

    def get_queryset(self):
        # Ensuring the results are displayed in order
        order_by = self.request.GET.get('order_by')
        queryset = Video.objects.all().order_by(order_by if order_by else '-published_at')

        # Implementing a simple search functionality
        search = self.request.GET.get('search')
        if search:
            search_words = search.split(' ')
            for word in search_words:
                queryset = queryset.filter(title__contains=word)

        return queryset
