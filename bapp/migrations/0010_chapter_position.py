# Generated by Django 3.2.8 on 2021-10-15 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0009_delete_chapterfiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='position',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
