
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from .models import Chapter, PostPage


class ChapterListView(ListView):

    model = Chapter
    template_name = 'manga/pages/home.html'
    context_object_name = 'chapters'


class PostPageView(DetailView):

    model = PostPage
    template_name = 'manga/pages/chapter.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Chapter, pk=self.kwargs.get('pk'))
