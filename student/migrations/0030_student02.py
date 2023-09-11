# Generated by Django 4.1.2 on 2023-09-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0029_alter_student01_first_name_alter_student01_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student02',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]