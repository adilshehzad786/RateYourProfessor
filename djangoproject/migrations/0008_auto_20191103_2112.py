# Generated by Django 2.2.6 on 2019-11-03 16:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0007_post_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
        ),
    ]
