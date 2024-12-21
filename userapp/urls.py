from django.contrib import admin
from django.urls import path, include
from userapp import views

urlpatterns = [
    path('index/', views.indexview2, name='index'),
    path('about/', views.aboutview, name='about'),
    path('product/', views.productview, name='product'),
    path('detail/<int:id>/', views.detailview, name='detail'),
    path('userregister/', views.userregisterview, name='user-register'),
    path('userlogin/', views.userloginview, name='user-login'),
    path('confirmpet/<int:id>/', views.confirmpet, name='confirmpet'),
    path('oderconfirm/', views.oderconfirm, name='oderconfirm'),
    path('orderlist/',views.orderlist,name='orderlist'),
    path('changepass/',views.changepass,name='changepass'),
    path('logout/',views.logoutview,name='logout')


]
