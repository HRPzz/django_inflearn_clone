# Generated by Django 4.1 on 2022-08-21 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0003_alter_mytext_board_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]