#from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import APIException
from rest_framework.decorators import action
from django.contrib.auth import authenticate, get_user_model, logout
from . import serializers
from . import models
from users.models import UserProfile

# Create your views here.
class ExpenseCreate(viewsets.ViewSet):
	permission_classes = [AllowAny, ]
	#@action(detail=True, methods=['post'],)
	def create(self, request):
		serializer = serializers.CreateExpenseSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		status_code = status.HTTP_201_CREATED
		response = {
			'success' : 'True',
			'status_code' : status_code,
			'message': 'Expense added successfully',
			'data': serializer.data
		}
		return Response(response, status=status_code)


class ExpenseListView(viewsets.ViewSet):
	permission_classes = [AllowAny, ]

	def list(self, request):
		queryset = models.Expense.objects.all()
		serializer = serializers.ListExpenseSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		queryset = models.Expense.objects.all()
		expense = get_object_or_404(queryset, pk=pk)
		serializer = serializers.HistoryExpenseSerializer(expense)
		return Response(serializer.data)

	#def get_uid(self, request):
	def get_data(self, request, *args, **kwargs):
		from_date = request.query_params.get('from')
		to_date = request.query_params.get('to')
		e_type = request.query_params.get('type')
		#values_list
		#queryset = User.objects.values_list('id')
		#if d_type == 'contract':
		# if e_type:
		# 	typ = ['contract', 'material', 'other']
		# 	if e_type not in typ:
		# 		raise APIException("Wrong type passed")
		#model.objects.raw('select form our row sql ');
		if from_date and to_date:
			if e_type:
				typ = ['contract', 'material', 'other', 'all']
				if e_type not in typ:
					raise APIException("Wrong type passed")
				if e_type == 'all':
					queryset = models.Expense.objects.filter(exp_date__gte=from_date, exp_date__lte=to_date)
				else:
					queryset = models.Expense.objects.filter(exp_date__gte=from_date, exp_date__lte=to_date, exp_type=e_type)
			else:
				queryset = models.Expense.objects.filter(exp_date__gte=from_date, exp_date__lte=to_date)
		else:
			raise APIException("Wrong params")
		#queryset = models.ConstContract.objects.raw('select id, c_name, start_date, c_father, expense.biller_name, expense.amount, expense.exp_date, expense.quantity, expense.rate, expense.remark from const_contract inner join expense on const_contract.expense_id = expense.id' )

		print(str(queryset.query))
		#c = models.ConstContract.objects.all()
		#pl = c.expense.all()

		# if d_type:
		# 	user = get_object_or_404(queryset, mobile=mobile)
		# elif uid:
		# 	user = get_object_or_404(queryset, id=uid)
		serializer = serializers.ListExpenseSerializer(queryset, many=True)
		#serializer = serializers.ContractExpSerializer(pl, many=True)
		return Response(serializer.data)


class UpdateExpenseView(UpdateAPIView,):
	queryset = models.Expense.objects.all()
	#lookup_field = 'id'
	permission_classes = (AllowAny,)
	serializer_class = serializers.UpdateExpenseSerializer
