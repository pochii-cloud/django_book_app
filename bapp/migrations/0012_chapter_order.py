# Generated by Django 3.2.8 on 2021-10-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0011_auto_20211015_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
