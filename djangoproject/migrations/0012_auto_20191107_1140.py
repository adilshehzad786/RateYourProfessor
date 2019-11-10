# Generated by Django 2.2.6 on 2019-11-07 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0011_auto_20191107_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='institute',
            field=models.CharField(choices=[(1, 'University of Central Punjab  '), (2, 'Lahore Medical And Dental College')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Average'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')], default=1),
        ),
    ]
