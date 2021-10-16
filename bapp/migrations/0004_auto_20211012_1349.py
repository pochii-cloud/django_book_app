# Generated by Django 3.2.4 on 2021-10-12 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0003_services_service_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='service_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bapp.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='service_img',
            field=models.ImageField(blank=True, upload_to='service_img', verbose_name='service Image'),
        ),
    ]
