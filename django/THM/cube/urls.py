# urls.py 
from django.urls import path 
from . import views

app_name = 'cube'
urlpatterns = [
	path('', views.index, name = 'index'),
]