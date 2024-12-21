from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from . import forms, models
from django.http import HttpResponse
from userapp.models import purchasepet
from django.db.models import Sum
# from userapp.views import indexview2
from django.contrib import messages




# Create your views here.

def indexview(request):
    if request.user.is_authenticated:
        data = models.pet.objects.all().count()
        abc = models.pet.objects.filter(isavailable=False).count()
        xyz = models.pet.objects.filter(isavailable=False).aggregate(total=Sum('price'))['total']
        return render(request, 'adminapp/admin-index.html', {'totaldog': data, 'selldog': abc, 'profit': xyz})
    else:
        return redirect(adminloginview)

def userindex(request):
    if request.user.is_authenticated:
        return render(request, 'userapp/index.html')
    else:
        return redirect(adminloginview)

def addpetsview(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = forms.petform(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.isavailable = True
                obj.save()
                messages.success(request, 'pets added successfully')

                return redirect(managepetsview)
            else:
                print(form.errors)
        return render(request, 'adminapp/add-pets.html')

    else:
        return redirect(adminloginview)


def managepetsview(request):

    if request.user.is_authenticated:
        data = models.pet.objects.all()
        context = {'data': data}
        return render(request, 'adminapp/manage-pets.html', context=context)
    else:
        return redirect(adminloginview)


def petsdeleteview(request, id):
    if request.user.is_authenticated:

        data = models.pet.objects.get(id=id)
        data.delete()
        messages.success(request, 'pets deleted successfully')
        return redirect(managepetsview)

    else:
        return redirect(adminloginview)


def petseditview(request, id):
    if request.user.is_authenticated:
        data = models.pet.objects.get(id=id)
        context = {'data': data}
        return render(request, 'adminapp/add-pets-edit.html', context=context)

    else:
        return redirect(adminloginview)


def petsupdateview(request, id):
    if request.user.is_authenticated:

        data = models.pet.objects.get(id=id)
        if request.method == "POST":
            form = forms.petform(request.POST, request.FILES, instance=data)
            if form.is_valid():
                form.save()
                messages.success(request, 'pets details updated successfully')
                return redirect(managepetsview)
            else:
                print(form.errors)
                return redirect(managepetsview)
        messages.success(request, 'pets details edited successfully')
        return render(request, 'adminapp/add-pets-edit.html')
    else:
        return redirect(adminloginview)


def adminregisterview(request):

    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('password1'):
            try:
                User.objects.get(username=request.POST.get('username'))
                return HttpResponse("user already exist")
            except:
                user = User.objects.create_user(username=request.POST.get('username'),
                                                email=request.POST.get('email'),
                                                password=request.POST.get('password'),
                                                is_superuser=True,
                                                )
                messages.success(request, 'Register successfully')

                return redirect(adminloginview)
        else:
            return HttpResponse("enter same password ")
    return render(request, 'adminapp/pages-register.html')


def adminloginview(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser == True:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect(indexview)
        elif user is not None and user.is_staff == True:
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect(userindex)
        else:
            return HttpResponse("User not found")

    return render(request, 'adminapp/pages-login.html')


def logoutview(request):

    logout(request)

    return redirect(adminloginview)


def changepass(request):
    messages.error(request, 'Change password successfully')
    return render(request, 'adminapp/changepass.html')


def orderlist1(request):
    if request.user.is_authenticated:
        data = purchasepet.objects.all()
        context = {'data': data}
        return render(request, 'adminapp/order_list.html', context=context)
    else:
        return redirect(adminloginview)


def userlist(request):
    if request.user.is_authenticated:
        data = User.objects.filter(is_staff = True)
        print(data)
        context = {'data': data}
        return render(request, 'adminapp/userlist.html', context=context)
    else:
        return redirect(adminloginview)


def search(request):
    if request.method == "POST":
        name = request.POST.get('type')
        print(name)
        data = models.pet.objects.get(name=name)
        print(data)
        return render(request, 'adminapp/search.html', {'data': data})
    return HttpResponse("Hello")

# def search(request):
#     if request.method == 'GET':
#         form = forms.petform(request.GET)
#         if form.is_valid():
#             query = form.cleaned_data['query']
#             results = models.pet.objects.filter(name__icontains=query)
#             return render(request, 'adminapp/search.html', {'results': results, 'query': query})
#     return render(request, 'adminapp/search.html')

def petsearch(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if name is not None:
            data = models.pet.objects.filter(name__icontains=name)
            print(data)
        else:
            data = models.pet.objects.all()
        context = {'data':data}
        return render(request,'adminapp/manage-pets.html',context)

