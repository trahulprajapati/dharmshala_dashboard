from rest_framework import routers
from django.conf.urls import url
from django.urls import path

#from .views import UserRegistrationView, UserLoginView
#from .views import AuthViewSet, ProfileView
from . import views

router = routers.DefaultRouter(trailing_slash=False)
#router.register('api/donation', views.AuthViewSet, basename='account')
#router.register('api/account', AuthViewSet, basename='account')
	
#urlpatterns = router.urls
urlpatterns = [
	path('api/donation/add', views.DonationCreate.as_view({'post': 'create'})),
	path('api/donation/list', views.DonationCreate.as_view({'get': 'list'})),
	# path('api/account/list/', views.UserListView.as_view({'get': 'list'})),
	path('api/donation/getdata', views.DonationCreate.as_view({'get': 'get_data'})),
	path('api/donation/update/<int:pk>', views.UpdateDonationView.as_view()),
	path('api/donation/list/<int:pk>', views.DonationCreate.as_view({'get' : 'retrieve'})),
	# path('api/account/reset_pwd/<int:mobile>', views.RestUserPwdView.as_view()),
]

urlpatterns += router.urls
# urlpatterns = [
# 	url(r'^register', UserRegistrationView.as_view()),
# 	url(r'^login', UserLoginView.as_view()),
# ]