# Generated by Django 2.2.6 on 2019-11-03 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0008_auto_20191103_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]
