
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Chapter, PostPage


class ChapterListView(ListView):

    model = Chapter
    template_name = 'manga/pages/home.html'
    context_object_name = 'chapters'


def viewPhoto(request, pk):
    photo = PostPage.objects.get(post_id=pk)
    return render(request, 'manga/pages/chapter.html', {'photo': photo})
