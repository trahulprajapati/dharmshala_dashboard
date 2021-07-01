from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords
from users.models import User

class Expense(models.Model):
	biller_name =  models.CharField('Name of shop', max_length=20, blank=False)
	amount = models.IntegerField('Amount of expense', blank=False)
	amount_type = models.CharField('Cash or check', max_length=10, blank=False)
	due = models.IntegerField('Due of expense if any', blank=True, null=True)
	check_number = models.CharField('Check number ', max_length=10, blank=True, null=True)
	remark = models.CharField('Description', max_length=30, blank=False)
	rate = models.CharField('Price per item', max_length=10, blank=False)
	exp_date = models.DateField(_("expense date"), default=datetime.date.today)
	quantity = models.CharField('Quantity ', max_length=10, blank=False)
	agent_id = models.ForeignKey(User, on_delete=models.CASCADE)
	history = HistoricalRecords() #HistoricalDonation model
	# contract_id = models.OneToOneField(Const_Contract, on_delete=models.CASCADE)
	# material_id = models.OneToOneField(Const_Material, on_delete=models.CASCADE)
	# other_id = models.OneToOneField(Exp_Other, on_delete=models.CASCADE)
	#history = HistoricalRecords() #HistoricalDonation model

	#REQUIRED_FIELDS = ['biller_name', 'amount']

	class Meta:
		db_table = 'expense'

# Create your models here.
class ExpenseType(models.Model):
	name = models.CharField('Expense Name', max_length=10, blank=False)
	description = models.CharField('Description of Expense', max_length=200, blank=False)

	class Meta:
		db_table = 'expense_type'

class ConstContract (models.Model):
	#c_owner = models.CharField('Contractor name', max_length=20, blank=False)
	c_father = models.CharField('Contractor father', max_length=20, blank=True, null=True)
	village = models.CharField('Contractor village', max_length=20, blank=False)
	mobile = models.CharField('Contractor mobile', max_length=20, blank=False)
	c_name = models.CharField('Contract name', max_length=20, blank=False)
	start_date = models.DateField('Contract start date', blank=False)
	due_date = models.DateField('Contract due date', blank=False)
	c_desc = models.CharField('Contract desription', max_length=50, blank=False)
	is_contract_new = models.BooleanField('Is contract new', default=True)
	is_contractor_new = models.BooleanField('Is contract new', default=True)
	expense = models.OneToOneField(Expense, on_delete=models.CASCADE, default='', related_name='contract' )
	history = HistoricalRecords() #HistoricalDonation model
	#rate = models.CharField('Name of expense', max_length=10, blank=False)
	#quantity = models.CharField('Name of expense', max_length=10, blank=False)

	class Meta:
		db_table = 'const_contract'

class ConstMaterial(models.Model):
	item_name = models.CharField('Contractor name', max_length=20, blank=False)
	#biller_name =  models.CharField('Name of shop', max_length=20, blank=False)
	item_from =   models.CharField('Shop/store', max_length=20, blank=False)
	bill_number =   models.CharField('Bill number', max_length=20, blank=False)
	item_type =   models.CharField('Item type-', max_length=20, blank=False)
	history = HistoricalRecords() #HistoricalDonation model
	expense = models.OneToOneField(Expense, on_delete=models.CASCADE, default='', related_name='material')

	class Meta:
		db_table = 'const_material'
	
# class Exp_Contruction(models.Model):
#     contract_id = models.ForeignKey(Const_Contract, on_delete=models.CASCADE)
#     material_id = models.ForeignKey(Const_Material, on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'exp_construction'

class ExpOther(models.Model):
	exp_name = models.CharField('Name of expense', max_length=10, blank=False)
	exp_for =  models.CharField('Expense for', max_length=20, blank=False)
	history = HistoricalRecords() #HistoricalDonation model
	expense = models.OneToOneField(Expense, on_delete=models.CASCADE, default='', related_name='other')
	#exp_type = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		db_table = 'exp_other'



