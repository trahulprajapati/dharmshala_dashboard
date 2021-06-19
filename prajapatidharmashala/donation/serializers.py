from rest_framework import serializers
import re
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from .models import Donation
from users.models import UserProfile
from users.serializers import UserSerializerGet
from prajapatidharmashala.settings import AUTH_USER_MODEL

#JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
#JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

Users = get_user_model()


class DonationSerializer(serializers.ModelSerializer):
	# name = serializers.CharField(required=True)
	# father = serializers.CharField(required=True)
	# village = serializers.CharField(required=False)
	# amount = serializers.IntegerField(required=False)

	agent_id = UserSerializerGet()

	class Meta:
		model = Donation
		fields = ('id', 'name', 'father', 'village', 'mobile', 'donation_type', 'amount', 
		'other', 'date', 'remark', 'due', 'agent_id')

	def create(self, validated_data):
		user = Donation.objects.create(**validated_data)
		return user

	# def update(self, instance, validated_data):
	# 	demo = Donation.objects.get(pk=instance.id)
	# 	Donation.objects.filter(pk=instance.id).update(**validated_data)
	# 	return demo

	# def update (self, instance, validated_data):
	# 	#print("---innn")
	# 	#demo = Donation.objects.get(pk=instance.id)
	# 	instance.name = validated_data.get('name', instance.name)
	# 	instance.father = validated_data.get('father', instance.father)
	# 	instance.village = validated_data.get('village', instance.village)
	# 	instance.amount = validated_data.get('amount', instance.amount)
	# 	instance.mobile = validated_data.get('mobile', instance.mobile)
	# 	instance.donation_type = validated_data.get('donation_type', instance.donation_type)
	# 	instance.other = validated_data.get('other', instance.other)
	# 	instance.remark = validated_data.get('remark', instance.remark)
	# 	instance.due = validated_data.get('due', instance.due)
	# 	instance.save

	# 	return instance

class UpdateDonationSerializer (serializers.ModelSerializer):
	agent_id = UserSerializerGet()

	class Meta:
		model = Donation
		fields = ('id', 'name', 'father', 'village', 'mobile', 'donation_type', 'amount', 
		'other', 'date', 'remark', 'due', 'agent_id')


class DonationHistorySerializer(serializers.ModelSerializer):
	history = serializers.SerializerMethodField(read_only=True)
	agent_id = UserSerializerGet()

	class Meta:
		#model = Donation.history.model
		model = Donation
		fields = ('id', 'name', 'father', 'village', 'mobile', 'donation_type', 'amount', 
		'other', 'date', 'remark', 'due', 'agent_id', 'history')
		read_only_fields = ('history',)

	def get_history(self, obj):
		history = obj.history.filter(id=obj.pk).values('history_date', 'remark', 'agent_id', 'amount', 'other' ).order_by('-history_date')
		return history

	# def get_profile(self, obj):
	# 	uid = self.get_agent_id
	# 	#name = UserProfile.objects.filter(user_id=uid).values('first_name', 'last_name')
	# 	#return obj.profile.filter(user_id=uid).values('first_name', 'last_name')
	# 	return obj.profile.filter(user_id=uid).values('first_name', 'last_name')
	# 	#return obj.agent_name.


	# def get_agent_id(self, obj):
	# 	return value