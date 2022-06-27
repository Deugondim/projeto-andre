
from django.shortcuts import render
from django.views.generic import ListView

from .models import Chapter, PostPage


class ChapterListView(ListView):

    model = Chapter
    template_name = 'manga/pages/home.html'
    context_object_name = 'chapters'


def viewPhoto(request, pk):
    chapter_id = Chapter.objects.get(chapter_number=pk).id
    photos = PostPage.objects.filter(post_id=chapter_id)
    photo = PostPage.objects.all()
    chapter_name = Chapter.objects.get(chapter_number=pk)
    chapter_number_link = Chapter.objects.get(chapter_number=pk).chapter_number
    next_chapter = chapter_number_link + 1
    previous_chapter = chapter_number_link - 1

    return render(request, 'manga/pages/chapter.html',
                  {'photo': photo, 'photos': photos,
                   'chapter_name': chapter_name,
                   'next_chapter': next_chapter,
                   'previous_chapter': previous_chapter,
                   'chapter_number_link': chapter_number_link})
