# Generated by Django 4.1.2 on 2023-09-06 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_remove_student01_phonenumber_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student01',
            name='phone_number',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
