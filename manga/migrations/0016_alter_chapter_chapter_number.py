# Generated by Django 4.0 on 2022-06-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0015_alter_chapter_chapter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_number',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]