from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.adminhome),
    path('viewusers/', views.viewusers),
    path('manageuserstatus/', views.manageuserstatus),
    path('addcat/', views.addcat),
    path('addsubcat/', views.addsubcat),
    path('addfoodproduct/', views.addfoodproduct),
    path('orderpaymentlistadmin/', views.orderpaymentlistadmin),
    path('changepasswordadmin/',views.changepasswordadmin)
]
