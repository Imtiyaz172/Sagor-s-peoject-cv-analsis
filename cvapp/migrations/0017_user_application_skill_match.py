# Generated by Django 2.0.3 on 2021-10-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0016_user_application_interviewlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_application',
            name='skill_match',
            field=models.IntegerField(default=0),
        ),
    ]
