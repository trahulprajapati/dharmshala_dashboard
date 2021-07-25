from rest_framework import routers
from django.conf.urls import url
from django.urls import path

from . import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
	path('api/expense/add', views.ExpenseCreate.as_view({'post': 'create'})),
	path('api/expense/list', views.ExpenseListView.as_view({'get': 'list'})),
	path('api/expense/list/<int:pk>', views.ExpenseListView.as_view({'get' : 'retrieve'})),
	path('api/expense/update/<int:pk>', views.UpdateExpenseView.as_view()),
	path('api/expense/getdata', views.ExpenseListView.as_view({'get': 'get_data'})),
]

urlpatterns += router.urls
# urlpatterns = [
# 	url(r'^register', UserRegistrationView.as_view()),
# 	url(r'^login', UserLoginView.as_view()),
# ]