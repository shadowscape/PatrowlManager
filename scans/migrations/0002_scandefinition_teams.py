# Generated by Django 2.2.13 on 2020-06-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200616_1704'),
        ('scans', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scandefinition',
            name='teams',
            field=models.ManyToManyField(blank=True, to='users.Team'),
        ),
    ]
