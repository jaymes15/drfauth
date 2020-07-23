from . import views
from django.conf.urls import url
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


app_name= 'authapiapp'
urlpatterns = [
	path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
	path('hello/', views.HelloView.as_view(), name='hello'),
	
	]