# Generated by Django 4.0.6 on 2022-07-14 05:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Username')),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last Name')),
                ('email', models.CharField(max_length=80, unique=True, verbose_name='Email')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
