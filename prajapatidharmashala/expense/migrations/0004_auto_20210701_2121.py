# Generated by Django 3.1.7 on 2021-07-01 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_delete_historicalexpense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constcontract',
            name='expense',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='expense.expense'),
        ),
        migrations.AlterField(
            model_name='constmaterial',
            name='expense',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='material', to='expense.expense'),
        ),
        migrations.AlterField(
            model_name='expother',
            name='expense',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, related_name='other', to='expense.expense'),
        ),
    ]
