from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.userhome),
    path('placeorder/', views.placeorder),
    path('orderpaymentlist/', views.orderpaymentlist),
    path('changepassworduser/',views.changepassworduser),
    path('editprofileuser/',views.editprofileuser)
]
