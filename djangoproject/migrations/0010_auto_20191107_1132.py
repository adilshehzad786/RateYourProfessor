# Generated by Django 2.2.6 on 2019-11-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0009_auto_20191103_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
    ]
