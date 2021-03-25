
# from django.contrib.auth import authenticate, get_user_model
# from rest_framework import serializers


# # def get_and_authenticate_user(email, password):
# # 	user = authenticate(username=email, password=password)
# # 	if user is None:
# # 		raise serializers.ValidationError("Invalid username/password. Please try again!")
# # 	return user

# def create_user_account(mobile, password, **extra_fields):
# 	user = get_user_model().objects.create_user(
# 		mobile=mobile, password=password,  **extra_fields)
# 	return user