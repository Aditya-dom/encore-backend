from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from myapp import views

urlpatterns = [
    path('0', views.index, name='user_login'),
    path('1',views.login,name='user_login'), 
    path('2',views.register,name='user_register'),
]

