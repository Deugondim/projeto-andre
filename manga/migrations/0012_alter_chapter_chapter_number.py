# Generated by Django 4.0 on 2022-06-27 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0011_alter_chapter_chapter_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='chapter_number',
            field=models.IntegerField(),
        ),
    ]
