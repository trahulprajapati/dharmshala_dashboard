from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
from simple_history.models import HistoricalRecords
from users.models import User
#from dharmashala_dashboard.prajapatidharmashala.users import models
# Create your models here.

class Donation(models.Model):
	agent_id = models.ForeignKey(User, on_delete=models.CASCADE)
	#agent_id = models.ForeignKey(User, on_delete=models.deletion.SET_NULL)
	name = models.CharField('Name', max_length=255, blank=False, null=False,default='')
	father = models.CharField('Father Name', max_length=30, blank=False, null=False)
	village = models.CharField('Village', max_length=20, blank=False, null=False)
	mobile = models.IntegerField('Mobile number')
	DONATION_TYPE = (
		('CONST', 'const'),
		('EVENT', 'event'),
		('OTHER', 'other')
	)
	DONATION_CHOICES = (
		('AMOUNT', 'amount'),
		('OTHER', 'other')
	)
	d_type =  models.CharField(choices=DONATION_TYPE, max_length=10, default='OTHER', blank=True, null=True )
	donation_type =  models.CharField(choices=DONATION_CHOICES, max_length=10)
	amount = models.IntegerField('Amount', default= 0)
	event_type = models.CharField('Event Type',  max_length=25, default= '', blank=True, null=True)
	other = models.CharField('other', max_length=255)
	date = models.DateField(_("date_joined"), default=datetime.date.today)
	remark = models.CharField('remark', max_length=255)
	due = models.IntegerField('Due', default=0)
	history = HistoricalRecords() #HistoricalDonation model

	REQUIRED_FIELDS = ['name', 'father', 'agent_id', 'village']

	class Meta:
		db_table = 'core_donation'


	def __str__(self):
		return '{} {} {} {}  '.format(self.name, self.father, self.village, self.mobile)


	# def get_full_name(self) -> str:
	# 	full_name = '{} {}'.format(self.first_name, self.last_name)
	# 	return full_name.strip()

# class DonationHistory(models.Model):
# 	donation_id = models.ForeignKey(User, on_delete=models.CASCADE)
# 	agent_id = models.ForeignKey(User, on_delete=models.CASCADE)
# 	name = models.CharField('Name', max_length=255, blank=False, null=False,default='')
# 	father = models.CharField('Father Name', max_length=30, blank=False, null=False)
# 	village = models.CharField('Village', max_length=20, blank=False, null=False)
# 	mobile = models.IntegerField('Mobile number')
# 	DONATION_CHOICES = (
# 		('AMOUNT', 'amount'),
# 		('OTHER', 'other')
# 	)
# 	donation_type =  models.CharField(choices=DONATION_CHOICES)
# 	amount = models.IntegerField('Amount', default= 0)
# 	other = models.CharField('other', max_length=255)
# 	date = models.DateField(_("date_joined"), default=datetime.date.today)
# 	remark = models.CharField('remark', max_length=255)
# 	due = models.IntegerField('Due', default=0)

# 	REQUIRED_FIELDS = ['name', 'father', 'agent_id', 'village']

# 	class Meta:
# 		db_table = 'core_donation'
