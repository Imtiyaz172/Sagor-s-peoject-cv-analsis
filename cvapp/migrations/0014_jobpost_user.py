# Generated by Django 2.0.3 on 2021-10-17 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cvapp', '0013_auto_20211017_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cvapp.Organization'),
        ),
    ]