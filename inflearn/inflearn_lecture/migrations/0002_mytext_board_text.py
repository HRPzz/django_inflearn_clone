# Generated by Django 4.1 on 2022-08-21 10:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='board_text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
