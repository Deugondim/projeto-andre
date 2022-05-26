import os

from django.db import models
from django.dispatch import receiver

# Create your models here.


class Chapter(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class PostPage(models.Model):
    post = models.ForeignKey(Chapter, default=None,
                             null=True, blank=True, on_delete=models.CASCADE)
    pages = models.ImageField(upload_to='manga/pages/')

    def __str__(self):
        return self.post.name


@ receiver(models.signals.post_delete, sender=PostPage)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.pages:
        if os.path.isfile(instance.pages.path):
            os.remove(instance.pages.path)


@receiver(models.signals.pre_save, sender=PostPage)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = PostPage.objects.get(pk=instance.pk).pages
    except PostPage.DoesNotExist:
        return False

    new_file = instance.pages
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
