from rest_framework import serializers
from .models import UserProfile, User

class UserProfileSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = UserProfile
		fields = ('first_name', 'last_name', 'father', 'village', 'alt_mobile', 'age', 'occupation', 'address', 'gender')


class UserRegisterSerializer(serializers.ModelSerializer):

	profile = UserProfileSerializer(required=False)

	class Meta:
		model = User
		fields = ('mobile', 'password', 'email', 'profile')
		extra_kwargs = {'password': {'write_only': True}}

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

		
class EmptySerializer(serializers.ModelSerializer):
	pass

