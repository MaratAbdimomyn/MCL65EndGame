# Generated by Django 5.0.1 on 2024-01-22 09:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('performer', models.CharField(max_length=112, verbose_name='Исполнитель')),
                ('song', models.CharField(max_length=112, verbose_name='Песня')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('image', models.ImageField(blank=True, upload_to='images', verbose_name='Фото')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
