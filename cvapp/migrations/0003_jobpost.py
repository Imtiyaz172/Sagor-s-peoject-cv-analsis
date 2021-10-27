# Generated by Django 2.0.3 on 2021-09-30 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0002_auto_20210922_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='jobpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=230)),
                ('vacency', models.CharField(max_length=230)),
                ('workplace', models.CharField(max_length=230)),
                ('job_location', models.CharField(max_length=230)),
                ('salary', models.CharField(max_length=230)),
                ('job_context', models.TextField(blank=True)),
                ('education_requirment', models.TextField(blank=True)),
                ('experience_requirment', models.TextField(blank=True)),
                ('additional_requirment', models.TextField(blank=True)),
                ('other_benifit_requirment', models.TextField(blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=1)),
            ],
        ),
    ]
