from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('menu',views.menu,name='menu'),
    path('single_category',views.single_category,name='single_category'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
]