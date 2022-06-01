
from django.shortcuts import render
from django.views.generic import ListView

from .models import Chapter, PostPage


class ChapterListView(ListView):

    model = Chapter
    template_name = 'manga/pages/home.html'
    context_object_name = 'chapters'


def viewPhoto(request, pk):

    photos = PostPage.objects.filter(post_id=pk)
    photo = PostPage.objects.all()
    chapter_name = Chapter.objects.get(id=pk)
    return render(request, 'manga/pages/chapter.html',
                  {'photo': photo, 'photos': photos,
                   'chapter_name': chapter_name})
