# Generated by Django 4.2.4 on 2023-08-17 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SMSApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gdr',
        ),
    ]
