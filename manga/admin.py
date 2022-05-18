from django.contrib import admin

from .models import Chapter, PostPage

# Register your models here.


class PostPageAdmin(admin.StackedInline):
    model = PostPage


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [PostPageAdmin]

    class Meta:
        model = Chapter
