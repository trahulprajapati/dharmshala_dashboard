# Generated by Django 3.1.7 on 2021-06-09 14:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mobile', models.IntegerField(db_index=True, unique=True, verbose_name='Mobile number')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_managmentuser', models.BooleanField(default=False)),
                ('is_commitymember', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'core_user',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(default='', max_length=255, verbose_name='Last Name')),
                ('father', models.CharField(max_length=30, verbose_name='Father Name')),
                ('village', models.CharField(max_length=20, verbose_name='Village')),
                ('alt_mobile', models.IntegerField(verbose_name='Alternative Mobile number')),
                ('age', models.IntegerField(default=0, verbose_name='Age')),
                ('occupation', models.CharField(default='NA', max_length=20, verbose_name='Occupation')),
                ('address', models.CharField(default='', max_length=255, verbose_name='Address')),
                ('date_joined', models.DateField(default=datetime.date.today, verbose_name='date_joined')),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female')], max_length=7)),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_profile',
            },
        ),
    ]
