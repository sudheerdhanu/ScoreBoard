# Generated by Django 3.1 on 2020-08-22 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20200821_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='points',
            field=models.IntegerField(null=True),
        ),
    ]