# Generated by Django 2.2.6 on 2019-11-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0020_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='agree_condition',
            field=models.BooleanField(default=False),
        ),
    ]
