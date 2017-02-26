from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login , logout

from .forms import RegisterForm , LoginForm
# Create your views here.
def home(request):
    print(request.user)
    return render(request,"index.html",context={'':""})

def _logout(request):
    logout(request)
    return redirect('home')

def _login(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request,"login.html",context={"form":form})
    elif request.method == 'POST':
        email    = request.POST.get('email')
        password = request.POST.get('password')
        user     = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print(user.email)
                return redirect('home')
        print("no success")
        return redirect('home')
        

def _register(request):
    if request.method =='GET':
        form = RegisterForm()
        return render(request,"register.html",context={"form":form})
    elif request.method == 'POST':
        pass

def profile(request):
    if request.method == 'GET':
        pass
    elif request.method =='POST':
        pass

