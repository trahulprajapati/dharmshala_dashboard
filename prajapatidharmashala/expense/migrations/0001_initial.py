# Generated by Django 3.1.7 on 2021-06-30 14:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biller_name', models.CharField(max_length=20, verbose_name='Name of shop')),
                ('amount', models.IntegerField(verbose_name='Amount of expense')),
                ('amount_type', models.CharField(max_length=10, verbose_name='Cash or check')),
                ('due', models.IntegerField(blank=True, verbose_name='Due of expense if any')),
                ('check_number', models.CharField(blank=True, max_length=10, verbose_name='Check number ')),
                ('remark', models.CharField(max_length=30, verbose_name='Description')),
                ('rate', models.CharField(max_length=10, verbose_name='Price per item')),
                ('exp_date', models.DateField(default=datetime.date.today, verbose_name='expense date')),
                ('quantity', models.CharField(max_length=10, verbose_name='Quantity ')),
                ('agent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'expense',
            },
        ),
        migrations.CreateModel(
            name='ExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Expense Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description of Expense')),
            ],
            options={
                'db_table': 'expense_type',
            },
        ),
        migrations.CreateModel(
            name='HistoricalExpense',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('biller_name', models.CharField(max_length=20, verbose_name='Name of shop')),
                ('amount', models.IntegerField(verbose_name='Amount of expense')),
                ('amount_type', models.CharField(max_length=10, verbose_name='Cash or check')),
                ('due', models.IntegerField(blank=True, verbose_name='Due of expense if any')),
                ('check_number', models.CharField(blank=True, max_length=10, verbose_name='Check number ')),
                ('remark', models.CharField(max_length=30, verbose_name='Description')),
                ('rate', models.CharField(max_length=10, verbose_name='Price per item')),
                ('exp_date', models.DateField(default=datetime.date.today, verbose_name='expense date')),
                ('quantity', models.CharField(max_length=10, verbose_name='Quantity ')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('agent_id', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical expense',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ExpOther',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_name', models.CharField(max_length=10, verbose_name='Name of expense')),
                ('exp_for', models.CharField(max_length=20, verbose_name='Expense for')),
                ('expense', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expense.expense')),
            ],
            options={
                'db_table': 'exp_other',
            },
        ),
        migrations.CreateModel(
            name='ConstMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20, verbose_name='Contractor name')),
                ('item_from', models.CharField(max_length=20, verbose_name='Shop/store')),
                ('bill_number', models.CharField(max_length=20, verbose_name='Bill number')),
                ('item_type', models.CharField(max_length=20, verbose_name='Item type-')),
                ('expense', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expense.expense')),
            ],
            options={
                'db_table': 'const_material',
            },
        ),
        migrations.CreateModel(
            name='ConstContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_father', models.CharField(blank=True, max_length=20, verbose_name='Contractor father')),
                ('village', models.CharField(max_length=20, verbose_name='Contractor village')),
                ('mobile', models.CharField(max_length=20, verbose_name='Contractor mobile')),
                ('c_name', models.CharField(max_length=20, verbose_name='Contract name')),
                ('start_date', models.DateField(verbose_name='Contract start date')),
                ('due_date', models.DateField(verbose_name='Contract due date')),
                ('c_desc', models.CharField(max_length=50, verbose_name='Contract desription')),
                ('is_contract_new', models.BooleanField(default=True, verbose_name='Is contract new')),
                ('is_contractor_new', models.BooleanField(default=True, verbose_name='Is contract new')),
                ('expense', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='expense.expense')),
            ],
            options={
                'db_table': 'const_contract',
            },
        ),
    ]
