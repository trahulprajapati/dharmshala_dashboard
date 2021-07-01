from rest_framework import routers
from django.conf.urls import url
from django.urls import path

from . import views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
	path('api/expense/add', views.ExpenseCreate.as_view({'post': 'create'})),
	#path('api/expense/list', views.ExpenseCreate.as_view({'get': 'list'})),
	path('api/expense/list', views.ExpenseListView.as_view({'get': 'list'})),
	path('api/expense/list/<int:pk>', views.ExpenseListView.as_view({'get' : 'retrieve'})),
	path('api/expense/update/<int:pk>', views.UpdateExpenseView.as_view()),
	# path('api/account/list/', views.UserListView.as_view({'get': 'list'})),
	# path('api/account/list/<int:mobile>', views.UserListView.as_view({'get': 'retrieve'})),
	# path('api/donation/update/<int:pk>', views.UpdateDonationView.as_view()),
	# path('api/donation/list/<int:pk>', views.DonationCreate.as_view({'get' : 'retrieve'})),
	# path('api/account/reset_pwd/<int:mobile>', views.RestUserPwdView.as_view()),
]

urlpatterns += router.urls
# urlpatterns = [
# 	url(r'^register', UserRegistrationView.as_view()),
# 	url(r'^login', UserLoginView.as_view()),
# ]