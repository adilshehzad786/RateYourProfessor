# Generated by Django 2.2.6 on 2019-11-07 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0018_auto_20191107_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='department',
            field=models.CharField(choices=[('Bachelor of Computer Science', 'Bachelor of Computer Science'), ('Bachelor of Software Engineering', 'Bachelor of Software Engineering')], default='Bachelor of Computer Science', max_length=50),
        ),
    ]
