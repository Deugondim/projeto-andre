from django.contrib import admin

from .models import Chapter, PostPage

# Register your models here.


class PostPageAdmin(admin.StackedInline):
    model = PostPage

    class Meta:
        model = Chapter


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    inlines = [PostPageAdmin]
