# Generated by Django 4.2.4 on 2023-09-11 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMSApp', '0046_reviewandrating_allo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='form',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]