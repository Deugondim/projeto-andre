# Generated by Django 4.0 on 2022-06-27 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0008_chapter_number_alter_postpage_pages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='number',
            new_name='chapter_number',
        ),
    ]
