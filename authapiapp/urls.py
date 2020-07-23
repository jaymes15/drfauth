from . import views
from .views import RegisterAPI,LoginAPI
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here
from knox import views as knox_views


app_name= 'authapiapp'
urlpatterns = [
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
	path('hello/', views.HelloView.as_view(), name='hello'),
	path('api/register/', RegisterAPI.as_view(), name='register'),
	path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
	
	]