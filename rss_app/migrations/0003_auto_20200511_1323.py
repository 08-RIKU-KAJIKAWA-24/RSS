# Generated by Django 2.2 on 2020-05-11 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rss_app', '0002_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='favorite_article_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
