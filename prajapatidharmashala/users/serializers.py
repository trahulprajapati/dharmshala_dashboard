from rest_framework import serializers
import re
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from .models import UserProfile, User

from prajapatidharmashala.settings import AUTH_USER_MODEL

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

Users = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'father', 'village', 'alt_mobile', 'age', 'occupation', 'address', 'gender')


class UserRegisterSerializer(serializers.ModelSerializer):

	profile = UserProfileSerializer(required=False)

	class Meta:
		model = User
		fields = ('mobile', 'password', 'email', 'profile')
		#fields = '__all__'#('mobile', 'password', 'email', 'profile')
		extra_kwargs = {'password': {'write_only': True}}

	def validate_mobile(self, value):
		#check if already tken
		user = User.objects.filter(mobile=value)
		if user:
			raise serializers.ValidationError("Mobile number already exist")
		return value

	def create(self, validated_data):	
		profile_data = validated_data.pop('profile')
		user = User.objects.create_user(**validated_data)
		UserProfile.objects.create(
			user = user,
			first_name = profile_data['first_name'],
			last_name = profile_data['last_name'],
			father = profile_data['father'],
			village = profile_data['village'],
			alt_mobile = profile_data['alt_mobile'],
			age = profile_data['age'],
			occupation = profile_data['occupation'],
			address = profile_data['address'],
			gender = profile_data['gender'],
		)
		return user


class UserLoginSerializers(serializers.Serializer):
	mobile = serializers.CharField(max_length=255)
	password = serializers.CharField(max_length=128, write_only=True)
	token = serializers.CharField(max_length=255, read_only=True)	

	def validate(self, data):
		mobile = data.get("mobile", None);
		password = data.get("password", None);

		#check if already tken
		users = Users.objects.filter(mobile=mobile)
		if users is None:
			raise serializers.ValidationError("User not exist")
		
		user = authenticate(username=mobile, password=password)
		if user is None:
			raise serializers.ValidationError("Username password incorrect")

		try:
			payload = JWT_PAYLOAD_HANDLER(user)
			jwt_token = JWT_ENCODE_HANDLER(payload)
			update_last_login(None, user)
		except User.DoesNotExist:
			raise serializers.ValidationError("Username/password does not exists")

		return {'mobile' : user.mobile, 'token' : jwt_token}


class EmptySerializer(serializers.Serializer):
	pass

