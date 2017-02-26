from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .models import Course,Department,User,Student,ExamPapers,Material,Announcements
from .forms import RegisterForm , LoginForm
from django.core import serializers
from django.contrib.auth.decorators import login_required
import json 
from django.http import JsonResponse,HttpResponse
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

def getDepartments(request):
    if request.method =='GET':
        dept = serializers.serialize("json",Department.objects.all(),use_natural_foreign_keys=True)
        data = json.loads(dept)
        result = {"result":data}
        return HttpResponse(json.dumps(result),content_type='application/json')


def getCourses(request,department=None):
    if request.method =='GET':
        dept   = get_object_or_404(Department,acronym=department)
        course = serializers.serialize("json",Course.objects.filter(dept=dept),use_natural_foreign_keys=True)
        data = json.loads(course)
        result = {"result":data}
        return HttpResponse(json.dumps(result),content_type='application/json')
        

