from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, login , logout
from .models import Course, Department, User, Student, ExamPaper, Material, Announcement
from .forms import RegisterForm , LoginForm , AnnouncementForm , MaterialForm , ExamPaperForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    print(request.user)
    return render(request,"index.html",context={'':""})

@login_required
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
@login_required
def Announcements(request,coursecode=None):
    if request.method =='GET':
        form= AnnouncementForm()
        return render(request,"announcements.html",context={"form":form})
    elif request.method =="POST":
        form = AnnouncementForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj=Announcement()
            obj.files = form.cleaned_data["files"]
            obj.title = form.cleaned_data["title"]
            obj.description = form.cleaned_data["description"]
            obj.author=request.user
            obj.course= Course.objects.get(code=coursecode)
            obj.save()
            print("Success")
            return redirect("home")
        print(form.errors)
        print("not successfull") 
        return redirect("home") 

@login_required
def Materials(request,coursecode=None):
    if request.method =='GET':
        form= MaterialForm()
        return render(request,"material.html",context={"form":form})
    elif request.method =="POST":
        form = MaterialForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj = Material()
            obj.files = form.cleaned_data["files"]
            obj.title = form.cleaned_data["title"]
            obj.author=request.user
            obj.course= Course.objects.get(code=coursecode)
            obj.save()
            print("Success")
            return redirect("home")
        print(form.errors)
        print("not successfull") 
        return redirect("home") 

@login_required
def ExamPapers(request,coursecode=None):
    if request.method =='GET':
        form= ExamPaperForm()
        return render(request,"ExamPaper.html",context={"form":form})
    elif request.method =="POST":
        form = ExamPaperForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj = ExamPaper()
            obj.files = form.cleaned_data["files"]
            obj.term = form.cleaned_data["term"]
            obj.author=request.user
            obj.course= Course.objects.get(code=coursecode)
            obj.save()
            print("Success")
            return redirect("home")
        print(form.errors)
        print("not successfull") 
        return redirect("home") 