# Generated by Django 4.2.4 on 2023-08-28 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_course', models.CharField(max_length=100)),
                ('user_room', models.CharField(max_length=100)),
                ('user_start', models.TimeField()),
                ('user_end', models.TimeField()),
                ('current_date', models.CharField(max_length=20)),
                ('current_day', models.CharField(max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
