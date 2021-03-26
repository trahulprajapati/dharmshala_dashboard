from rest_framework import routers
from django.conf.urls import url
from django.urls import path

#from .views import UserRegistrationView, UserLoginView
from .views import AuthViewSet, ProfileView

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/account', AuthViewSet, basename='account')
#router.register('api/account', AuthViewSet, basename='account')
	
#urlpatterns = router.urls
urlpatterns = [
	path('api/account/profile/', ProfileView.as_view()),
]

urlpatterns += router.urls
# urlpatterns = [
# 	url(r'^register', UserRegistrationView.as_view()),
# 	url(r'^login', UserLoginView.as_view()),
# ]