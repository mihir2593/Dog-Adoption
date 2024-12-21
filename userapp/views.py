from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from adminapp.models import pet
from . import models
from . import forms
from adminapp.views import adminloginview
from adminapp.views import indexview


def indexview2(request):
    if request.user.is_authenticated:
        return render(request, 'userapp/index.html')
    else:
        return redirect(userloginview)


def aboutview(request):
    if request.user.is_authenticated:
        return render(request, 'userapp/about.html')
    else:
        return redirect(userloginview)


def productview(request):
    if request.user.is_authenticated:
        data = pet.objects.filter(isavailable=True )
        paginator =Paginator(data,2)
        page_number=request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        abc={
            'data':page_obj,
        }
        return render(request, 'userapp/product.html',abc)
    else:
        return redirect(userloginview)


def detailview(request, id):
    if request.user.is_authenticated:
        data = pet.objects.get(id=id)
        context = {'data': data}
        return render(request, 'userapp/detail.html', context=context)
    else:
        return redirect(userloginview)


def userregisterview(request):
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse("user already exist")
            except:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password'),
                                                is_staff= True,)
                return redirect(userloginview)
        else:
            return HttpResponse("enter same password ")
    return render(request, 'userapp/pages-register.html')


def userloginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser == True:
            login(request, user)
            return redirect(indexview)
        elif user is not None and user.is_staff == True:
            login(request, user)
            return redirect(indexview2)
        else:
            return HttpResponse("User not found")
    return render(request, 'userapp/pages-login.html')


def logoutview(request):
    logout(request)
    return redirect(userloginview)


def confirmpet(request, id):
    if request.user.is_authenticated:
        petdata = pet.objects.get(id=id)
        if request.method == "POST":
            data = models.purchasepet()
            data.user = request.user
            data.pe = petdata
            data.save()
            petdata.isavailable = False
            petdata.save()
            return redirect(oderconfirm)
        return render(request, 'userapp/detail.html')
    else:
        return redirect(userloginview)


def oderconfirm(request):
    if request.user.is_authenticated:
        return render(request, 'userapp/orderconfirm.html')
    else:
        return redirect(userloginview)


def orderlist(request):
    if request.user.is_authenticated:
        data = models.purchasepet.objects.filter(user=request.user)
        context = {'data': data}
        return render(request, 'userapp/order_list.html', context=context)
    else:
        return redirect(userloginview)

def changepass(request):
    if request.method == "POST":
        form = forms.changepassform(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect(indexview2)
        else:
            print(form.errors)
    return render(request, 'userapp/changepass.html')
