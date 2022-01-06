from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('viewsubcat/', views.viewsubcat),
    path('viewfoodproduct/', views.viewfoodproduct),
    path('orderlogin/', views.orderlogin),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('register/', views.register),
    path('verifyuser/', views.verifyuser),
    path('login/', views.login),
    path('payment/', views.payment),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('myadmin/', include('myadmin.urls')),
    path('user/', include('user.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
