from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm


from biodata . models import Biodata


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'index.html', {'name': name})
    else: 
        return render(request, 'index.html', {})

def about(request):
    template_name = 'about.html'
    data = Biodata.objects.all()
    for d in data:
        print(d.user, d.nama, d.telp, d.alamat)
    print(data)
    context = {
        'title' : 'my about',
        'welcome': 'Welcome to my about',
        'data' : data,
    }
    return render(request, template_name, context)

def registerPage (request):
    form = UserCreationForm()
    if request. method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('login')
           
    context = {'form':form}
    return render(request, 'account/register.html', context)

def login(request):
    template_name = "account/login.html"
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('benar')
            auth_login(request, user)
            return redirect('index')
        else:
            #data tidakada
            print('salah')
            return redirect('login')
    context = {
        'title' : 'form login'
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('index')

