# Generated by Django 4.1.1 on 2022-11-14 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('free', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='free',
            name='hashtags',
            field=models.ManyToManyField(blank=True, null=True, to='main.hashtag'),
        ),
        migrations.AddField(
            model_name='free',
            name='p_like',
            field=models.ManyToManyField(blank=True, related_name='f_like_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='free',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
