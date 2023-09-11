# Generated by Django 4.1.2 on 2023-09-06 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0014_student01_email_student01_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='John', max_length=100)),
                ('last_name', models.CharField(default='John', max_length=100)),
                ('user_name', models.CharField(default='John', max_length=100)),
                ('password', models.CharField(default='John', max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('verification_token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('phoneNumber', models.CharField(default='', max_length=15)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='studentupdate',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.user'),
        ),
    ]