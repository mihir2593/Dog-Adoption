from django.contrib import admin
from django.urls import path, include
from adminapp import views

urlpatterns = [
    path('index/', views.indexview, name='index-view'),
    path('userindex/', views.userindex, name='index'),

    path('add-pets/', views.addpetsview, name='add-pets'),
    path('manage-pets/', views.managepetsview, name='manage-pets'),
    path('petsdelete/<int:id>/',views.petsdeleteview, name='pets-delete'),
    path('petsedit/<int:id>/',views.petseditview, name='pets-edit'),
    path('petsupdate/<int:id>/', views.petsupdateview, name='pets-update'),
    path('adminregister/', views.adminregisterview, name='admin-register'),
    path('adminlogin/', views.adminloginview, name='admin-login'),
    path('changepass/', views.changepass, name='changepass'),
    path('orderlist1/',views.orderlist1,name='orderlist1'),
    path('userlist/',views.userlist,name='userlist'),
    path('search_data/',views.search,name='search_data'),
    path('petsearch/', views.petsearch, name='petsearch'),

]
