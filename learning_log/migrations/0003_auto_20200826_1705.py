# Generated by Django 2.1 on 2020-08-26 09:05

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0002_auto_20200826_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningcontent',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='内容'),
        ),
    ]
