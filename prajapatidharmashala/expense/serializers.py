from rest_framework import serializers
from . import models
from users.models import UserProfile
from users.serializers import UserSerializerGet

class ContractExpSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ConstContract
		fields = ('id', 'c_father', 'village', 'mobile', 'c_name', 'start_date', 'due_date',
			'c_desc', 'is_contract_new', 'is_contractor_new', 'expense' )
		
class ContractUpdateExpSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ConstContract
		fields = ('id', 'mobile', 'due_date', 'c_desc' )
		read_only_fields = ('id',)

class MaterialExpSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ConstMaterial
		fields = ('id', 'item_name', 'item_from', 'bill_number', 'item_type', 'expense')


class OtherExpSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.ExpOther
		fields = ('id', 'exp_name', 'exp_for', 'expense')


class CreateExpenseSerializer(serializers.ModelSerializer):
	contract_exp = ContractExpSerializer(required=False)
	material_exp = MaterialExpSerializer(required=False)
	other_exp = OtherExpSerializer(required=False)
	
	class Meta:
		model = models.Expense
		fields = ('id', 'biller_name', 'amount', 'amount_type', 'exp_name', 'due', 'check_number', 'remark', 'rate',
			'exp_date', 'quantity', 'agent_id', 'exp_type', 'contract_exp', 'material_exp', 'other_exp')
		#'other', 'date', 'remark', 'due', 'agent_id')
		#fields = '__all__'

	# def create(self, validated_data):
	# 	user = Donation.objects.create(**validated_data)
	# 	return user
	def create(self, validated_data):
		contact_data = validated_data.get('contract_exp')
		if contact_data:
			contact_data = validated_data.pop('contract_exp')
		
		material_data = validated_data.get('material_exp')
		if material_data:
			material_data = validated_data.pop('material_exp')
		
		other_data = validated_data.get('other_exp')
		if other_data:
			other_data = validated_data.pop('other_exp')

		expense = models.Expense.objects.create(**validated_data)

		if contact_data:
			models.ConstContract.objects.create(
				expense = expense,
				c_father = contact_data['c_father'],
				village = contact_data['village'],
				mobile = contact_data['mobile'],
				c_name = contact_data['c_name'],
				start_date = contact_data['start_date'],
				due_date = contact_data['due_date'],
				c_desc = contact_data['c_desc'],
				is_contract_new = contact_data['is_contract_new'],
				is_contractor_new = contact_data['is_contractor_new'],
			)
		if material_data:
			models.ConstMaterial.objects.create(
				expense = expense,
				item_name = material_data['item_name'],
				item_from = material_data['item_from'],
				bill_number = material_data['bill_number'],
				item_type = material_data['item_type'],
			)

		if other_data:
			models.ExpOther.objects.create(
				expense = expense,
				exp_name = other_data['exp_name'],
				exp_for = other_data['exp_for']
			)

		return expense

class ListExpenseSerializer(serializers.ModelSerializer):
	contract = ContractExpSerializer(required=False)
	material = MaterialExpSerializer(required=False)
	other = OtherExpSerializer(required=False)
	agent_id = UserSerializerGet()
	
	class Meta:
		model = models.Expense
		fields = ('id', 'biller_name', 'exp_name', 'amount', 'amount_type', 'due', 'check_number', 'remark', 'rate',
			'exp_date', 'quantity', 'agent_id',  'contract', 'material', 'exp_type', 'other')
		read_only_fields = ('id','agent_id', 'contract', 'material', 'other')
		#'other', 'date', 'remark', 'due', 'agent_id')
		#fields = '__all__'

class UpdateExpenseSerializer(serializers.ModelSerializer):
	#contract = ContractUpdateExpSerializer(required=False)
	class Meta:
		model = models.Expense
		fields = ('id', 'amount', 'amount_type', 'due', 'remark', 'rate',
			'quantity', 'agent_id')
		read_only_fields = ('id','agent_id',)


class HistoryExpenseSerializer(serializers.ModelSerializer):
	contract = ContractExpSerializer(required=False)
	material = MaterialExpSerializer(required=False)
	other = OtherExpSerializer(required=False)
	history = serializers.SerializerMethodField(read_only=True)
	agent_id = UserSerializerGet()

	class Meta:
		model = models.Expense
		fields = ('id', 'biller_name', 'amount', 'exp_name', 'amount_type', 'due', 'check_number', 'remark', 'rate',
			'exp_date', 'quantity', 'agent_id', 'history', 'contract', 'material', 'other','exp_type',)
		read_only_fields = ('history',)

	def get_history(self, obj):
		history = obj.history.filter(id=obj.pk).values('history_date', 'remark', 'agent_id', 'amount', 'biller_name' ).order_by('-history_date')
		return history