from django.db import models
import datetime
import uuid
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
# Create your models here.


# class Role(models.Model):
# 	MANAGEMENT = 1
# 	COMMITYMEMBER = 2
# 	ADMIN = 3

# 	ROLE_CHOICES = (
# 		(MANAGEMENT, 'managament'),
# 		(COMMITYMEMBER, 'commitymember'),
# 		(ADMIN, 'admin'),
# 	)

# 	id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

# 	def __str__(self):
# 		return self.get_id_display()


class UserManager(BaseUserManager):

	def create_user(self, mobile, password, **extra_fields):
		if not mobile:
			raise ValueError('Users Must Have an email address')

		user = self.model(mobile=mobile, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(mobile, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
	
	def create_managmentuser(mobile, password, **extra_fields):
		if not mobile:
			raise ValueError('Users Must Have an email address')

		user = self.create_user(mobile, password, **extra_fields)
		user.set_password(password)
		user.is_managmentuser = True
		user.save()
		return user

	def create_commitymemberuser(mobile, password, **extra_fields):
		if not mobile:
			raise ValueError('Users Must Have an email address')

		user = self.create_user(mobile, password, **extra_fields)
		user.set_password(password)
		user.is_commitymember = True
		user.save()
		return user


class User(AbstractBaseUser):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	mobile = models.IntegerField('Mobile number', blank=False, unique=True, null=False)
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True
	)
	is_active = models.BooleanField(default=True)
	is_superuser = models.BooleanField(default=False)
	is_managmentuser = models.BooleanField(default=False)
	is_commitymember = models.BooleanField(default=False)
	USERNAME_FIELD = 'mobile'
	objects = UserManager()

	class Meta:
		db_table = 'core_user'



class UserProfile(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	user = models.OneToOneField(User, on_delete=models.CASCADE, default='', related_name='profile')
	#roles = models.ManyToManyField(Role)
	first_name = models.CharField('First Name', max_length=255, blank=False, null=False,default='')
	last_name = models.CharField('Last Name', max_length=255, blank=False, null=False, default='')
	father = models.CharField('Father Name', max_length=30, blank=False, null=False)
	village = models.CharField('Village', max_length=20, blank=False, null=False)
	alt_mobile = models.IntegerField('Alternative Mobile number')
	age = models.IntegerField('Age', default=0)
	occupation = models.CharField('Last Name', max_length=20, blank=False, null=False,  default='NA')
	address = models.CharField('address', max_length=255, blank=False, null=False,  default='')
	date_joined = models.DateField(_("date_joined"), default=datetime.date.today)
	USER_CHOICES = (
		('MALE', 'male'),
		('FEMALE', 'female')
	)
	gender = models.CharField(choices=USER_CHOICES, max_length=7)
	REQUIRED_FIELDS = ['first_name', 'last_name', 'father', 'gender', 'village']

	class Meta:
		db_table = 'core_profile'


	def get_full_name(self) -> str:
		full_name = '{} {}'.format(self.first_name, self.last_name)
		return full_name.strip()

