# Generated by Django 4.2.4 on 2023-08-29 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMSApp', '0009_alter_user_pfimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pfimg',
            field=models.ImageField(default='profile.jpg', upload_to='images/'),
        ),
    ]
