# Generated by Django 5.1.6 on 2025-03-01 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
    ]
