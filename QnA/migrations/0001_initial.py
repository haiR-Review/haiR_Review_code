# Generated by Django 4.1.2 on 2022-10-28 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=50)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('a_photo', models.ImageField(blank=True, null=True, upload_to='a_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('q_date', models.DateTimeField(verbose_name='data published')),
                ('q_photo', models.ImageField(blank=True, null=True, upload_to='q_images/')),
                ('q_clicks', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('q_likes', models.PositiveIntegerField(default=0, verbose_name='추천수')),
            ],
        ),
    ]
