# Generated by Django 2.0 on 2018-12-28 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0014_auto_20181228_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='detail',
        ),
    ]
