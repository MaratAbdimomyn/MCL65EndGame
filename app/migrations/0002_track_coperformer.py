# Generated by Django 5.0.1 on 2024-01-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='coperformer',
            field=models.CharField(default=1, max_length=112, verbose_name='Соисполнитель'),
            preserve_default=False,
        ),
    ]
