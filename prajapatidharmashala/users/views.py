from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from django.contrib.auth import authenticate, get_user_model

from . import serializers

User = get_user_model()

class AuthViewSet(viewsets.GenericViewSet):
	permission_classes = [AllowAny, ]
	serializer_class = serializers.UserRegisterSerializer
	queryset = ''
	serializer_classes = {
		'register': serializers.UserRegisterSerializer
	}

	#registeer
	@action(methods=['POST', ], detail=False)
	def register(self, request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		status_code = status.HTTP_201_CREATED
		response = {
			'success' : 'True',
			'status code' : status_code,
			'message': 'User registered  successfully',
		}
		return Response(response, status=status_code)
		# user = create_user_account(**serializer.validated_data)
		# data = serializers.AuthUserSerializer(user).data
		# return Response(data=data, status=status.HTTP_201_CREATED)
