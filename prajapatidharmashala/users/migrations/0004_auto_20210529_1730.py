# Generated by Django 3.1.7 on 2021-05-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210529_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(db_index=True, unique=True, verbose_name='Mobile number'),
        ),
    ]