# Generated by Django 2.2.6 on 2019-11-07 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0017_auto_20191107_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.CharField(choices=[('Poor', 'Poor'), ('Average', 'Average'), ('Good', 'Good'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], default='Poor', max_length=10),
        ),
    ]
