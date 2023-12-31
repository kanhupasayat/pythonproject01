# Generated by Django 4.1.2 on 2023-09-06 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0006_remove_student01_mobile_number_student01_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phoneNumber', models.CharField(default=0, max_length=16, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
