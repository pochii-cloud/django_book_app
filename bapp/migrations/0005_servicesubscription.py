# Generated by Django 3.2.4 on 2021-10-12 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0004_auto_20211012_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='servicesubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', models.CharField(max_length=100, verbose_name='Subscription ID ')),
                ('txn_date', models.DateTimeField(blank=True)),
                ('exp_date', models.DateTimeField(blank=True)),
                ('txn_id', models.CharField(max_length=100, verbose_name='Invoice ID')),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('service_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bapp.services')),
            ],
            options={
                'ordering': ['txn_date'],
            },
        ),
    ]