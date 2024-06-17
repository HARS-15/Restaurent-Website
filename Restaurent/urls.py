from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.main,name='main'),
    path('menu',views.menu,name='menu'),
    path('single_category/<int:menu_id>/',views.single_category,name='single_category'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('profile',views.profile,name='profile'),
    path('ordered_items',views.ordered_items,name="ordered_items"),
    path('logout',views.logout,name='logout'),
    path("place_order",views.place_order,name="place_order"),
    path("order",views.order,name="order"),
    path("remove",views.remove,name="remove")
]