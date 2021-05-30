from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import action
from django.contrib.auth import authenticate, get_user_model, logout
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import UserProfile
from . import serializers


User = get_user_model()

class AuthViewSet(viewsets.GenericViewSet):
	permission_classes = [AllowAny, ]
	#serializer_class = serializers.UserRegisterSerializer
	serializer_class = serializers.EmptySerializer	
	queryset = ''
	serializer_classes = {
		'register': serializers.UserRegisterSerializer,
		'login': serializers.UserLoginSerializers
	}

	#register
	@action(methods=['POST', ], detail=False)
	def register(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		status_code = status.HTTP_201_CREATED
		response = {
			'success' : 'True',
			'status_code' : status_code,
			'message': 'User registered  successfully',
		}
		return Response(response, status=status_code)

		#register
	# @action(methods=['PUT', ], detail=False)
	# def update(self, request, mobile=None):
	# 	serializer = self.get_serializer(data=request.data)
	# 	serializer.is_valid(raise_exception=True)
	# 	serializer.save()
	# 	status_code = status.HTTP_201_CREATED
	# 	response = {
	# 		'success' : 'True',
	# 		'status_code' : status_code,
	# 		'message': 'User registered  successfully',
	# 	}
	# 	return Response(response, status=status_code)

	#login
	@action(methods=['POST', ], detail=False)
	def login(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		status_code = status.HTTP_200_OK
		response = {
			'success' : 'True',
			'status_code' : status_code,
			'message': 'User logged  successfully',
			'token' : serializer.data['token'],
			'mobile' : serializer.data['mobile'],
			#'serializer' : serializer.data
		}
		return Response(response, status=status_code)

	@action(methods=['POST', ], detail=False)
	def logout(self, request):
		logout(request)
		status_code = status.HTTP_200_OK
		res = {
			'status_code' : status_code,
			'success': 'Sucessfully logged out'
		}
		return Response(data=res, status=status_code)

	def get_serializer_class(self):
		if not isinstance(self.serializer_classes, dict):
			raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

		if self.action in self.serializer_classes.keys():
			return self.serializer_classes[self.action]
		return super().get_serializer_class()


#profile view
class ProfileView(RetrieveAPIView):
	permission_classes = (IsAuthenticated,)
	authentication_class = JSONWebTokenAuthentication

	def get(self, request):
		try:
			profile = UserProfile.objects.get(user=request.user)
			status_code = status.HTTP_200_OK
			res = {
				'success' : 'true',
				'status_code' : status_code,
				'message' : 'Profile fetched successfully',
				'data' : [{
					'first_name' : profile.first_name,
					'last_name' : profile.last_name,
					'father': profile.father,
					'village' : profile.village,
					'alt_mobile' : profile.alt_mobile,
					'age' : profile.age,
					'occupation' : profile.occupation,
					'address' : profile.address,
					'gender' : profile.gender
				}]
			}
		except Exception as e:
			status_code = status.HTTP_400_BAD_REQUEST
			res = {
				'success' : 'false',
				'status_code' : status_code,
				'message' : 'User does not exists',
				'error': str(e)
			}
		return Response(res, status=status_code)

#list 
class UserListView(viewsets.ViewSet):
	permission_classes = [AllowAny, ]

	def list(self, request):
		queryset = User.objects.all()
		serializer = serializers.UserRegisterSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, mobile):
		queryset = User.objects.all()
		user = get_object_or_404(queryset, mobile=mobile)
		serializer = serializers.UserRegisterSerializer(user)
		return Response(serializer.data)



class UpdateUserProfileView(UpdateAPIView,):
	queryset = User.objects.all()
	lookup_field = 'mobile'
	permission_classes = (IsAuthenticated,)
	serializer_class = serializers.UpdateUserSerializer

	# def update(self, request, *args, **kwargs):
	# 	profile = kwargs.pop('profile', False)
	# 	instance = self.get_object()
	# 	serializer = self.get_serializer(instance, data=request.data, partial=profile)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.perform_update(serializer)
	# 	result = {
	# 	"message": "success",
	# 	"details": serializer.data,
	# 	"status": 200,

	# 	}
	# 	return Response(result)



class RestUserPwdView(UpdateAPIView):

	queryset = User.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = serializers.RestPwdSerializer

