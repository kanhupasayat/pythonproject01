# Generated by Django 4.1.2 on 2023-09-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_student01_mobile_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student01',
            name='mobile_number',
        ),
        migrations.AddField(
            model_name='student01',
            name='phoneNumber',
            field=models.CharField(default=0, max_length=16, unique=True),
        ),
    ]
