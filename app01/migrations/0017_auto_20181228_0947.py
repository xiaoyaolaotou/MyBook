# Generated by Django 2.0 on 2018-12-28 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_author_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
        migrations.RemoveField(
            model_name='author',
            name='detail',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
