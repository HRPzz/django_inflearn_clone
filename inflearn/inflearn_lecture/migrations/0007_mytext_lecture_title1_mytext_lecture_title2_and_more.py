# Generated by Django 4.1 on 2022-08-23 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='lecture_title1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_title2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_title3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_title4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_video1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_video2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_video3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mytext',
            name='lecture_video4',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
