# Generated by Django 3.1.7 on 2021-06-30 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20210630_1955'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HistoricalExpense',
        ),
    ]
