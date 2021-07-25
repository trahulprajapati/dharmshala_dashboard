from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.decorators import action
from django.contrib.auth import authenticate, get_user_model, logout
from . import serializers
from .models import Donation
from users.models import UserProfile
# Create your views here.

#User = get_user_model()

class DonationCreate(viewsets.ViewSet):
	permission_classes = [AllowAny, ]
	#@action(detail=True, methods=['post'],)
	def create(self, request):
		serializer = serializers.DonationSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		status_code = status.HTTP_201_CREATED
		response = {
			'success' : 'True',
			'status_code' : status_code,
			'message': 'Donation registered  successfully',
			'data': serializer.data
		}
		return Response(response, status=status_code)

	def list(self, request):
		queryset = Donation.objects.all()
		serializer = serializers.ListDonationSerializer(queryset, many=True)
		# donation_data = list(serializer.data)
		# for ref in donation_data:
		# 	ref['agent_id'] = ref['agent_id']['']
		# 	del ref[]
		# for k in donation_data:
		# 	kval11 = donation_data[k]
		# 	kval11['agent_name'] = kval11['agent_id']['first_name']
			# for k2 in kval11:
			# 	kval11['agent_name'] = kval11[k2]
		#donation_data['agent_name'] = str('gtesssssssssssss')
		return Response(serializer.data)

	# def list(self, request):
	# 	queryset = Donation.objects.all()
	# 	serializer = serializers.DonationSerializer(queryset, many=True)
	# 	return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = Donation.objects.all()
		user = get_object_or_404(queryset, pk=pk)
		#profile = UserProfile.objects.all()
		serializer = serializers.DonationHistorySerializer(user)
		return Response(serializer.data)

	def get_data(self, request, *args, **kwargs):
		from_date = request.query_params.get('from')
		to_date = request.query_params.get('to')
		e_type = request.query_params.get('type')
		#validate
		if from_date and to_date:
			if e_type:
				typ = ['CONST', 'EVENT', 'OTHER', 'ALL']
				if e_type not in typ:
					raise APIException("Wrong type passed")
				if e_type == 'ALL':
					queryset = Donation.objects.filter(date__gte=from_date, date__lte=to_date)
				else:
					queryset = Donation.objects.filter(date__gte=from_date, date__lte=to_date, d_type=e_type)
			else:
				queryset = Donation.objects.filter(date__gte=from_date, date__lte=to_date)
		else:
			raise APIException("Wrong params")

		print(str(queryset.query))
		serializer = serializers.ListDonationSerializer(queryset, many=True)
		#serializer = serializers.ContractExpSerializer(pl, many=True)
		return Response(serializer.data)

	#def update(self, request):
	def partial_update(self, request, pk=None):
		serializer = serializers.DonationSerializer(data=request.data, partial=True)
		#self.perform_update(serializer)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		# queryset = Donation.objects.all()
		# serializer = serializers.DonationSerializer(queryset, many=True)
		return Response(status=status.HTTP_202_ACCEPTED)
	
	# def get_permissions(self):
	# 	permission_classes = [AllowAny, ]
	# 	return [permission() for permission in permission_classes]


class UpdateDonationView(UpdateAPIView,):
	queryset = Donation.objects.all()
	#lookup_field = 'id'
	permission_classes = (AllowAny,)
	serializer_class = serializers.UpdateDonationSerializer


