# Generated by Django 2.0 on 2018-12-28 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0015_remove_person_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='detail',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
        ),
    ]
