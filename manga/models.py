from django.db import models

# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class PostPage(models.Model):
    post = models.ForeignKey(Chapter, default=None, on_delete=models.CASCADE)
    pages = models.FileField(upload_to='manga/static/manga/pages/')

    def __str__(self):
        return self.post.title
