# Generated by Django 2.2.6 on 2019-11-02 05:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='institute',
            field=models.CharField(default=datetime.datetime(2019, 11, 2, 5, 55, 36, 904499, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
