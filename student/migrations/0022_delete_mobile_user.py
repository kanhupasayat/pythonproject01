# Generated by Django 4.1.2 on 2023-09-07 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_alter_mobile_user_user_mobile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='mobile_user',
        ),
    ]