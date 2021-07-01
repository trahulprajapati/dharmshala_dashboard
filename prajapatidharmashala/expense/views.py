#from django.shortcuts import render
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
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

class UpdateExpenseView(UpdateAPIView,):
	queryset = models.Expense.objects.all()
	#lookup_field = 'id'
	permission_classes = (AllowAny,)
	serializer_class = serializers.UpdateExpenseSerializer
