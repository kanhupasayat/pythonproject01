# Generated by Django 4.1.2 on 2023-09-06 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_student01_phonenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student01',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='is_verified',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='password',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='student01',
            name='verification_token',
        ),
        migrations.AlterField(
            model_name='student01',
            name='phoneNumber',
            field=models.CharField(max_length=10),
        ),
    ]
