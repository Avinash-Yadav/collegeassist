from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , logout
from .models import Course, Department, User, Student, ExamPaper, Material, Announcement, CourseAllotment, Bookmark, Feedback, Contributor, Stat
from .forms import RegisterForm , LoginForm , AnnouncementForm , MaterialForm , ExamPaperForm, FeedbackForm, AvatorForm, ForgetPasswordForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse,HttpResponse
from django.urls import reverse
import datetime
import json
rewardvalue=5
# Create your views here.
def home(request):
    if request.user.is_anonymous():
        return render(request,"feed.html",context={})
    bookmarks  =Bookmark.objects.filter(user=request.user)
    bookmarkcourses = Bookmark.objects.select_related('course').filter(user=request.user)
    courselist=[]
    for bookmark in bookmarks:
        courselist.append(bookmark.course)
    start_from = int(request.GET.get('start_from',0))
    announcements = Announcement.objects.select_related('author').filter(course__in=courselist).order_by('-updated_on')[start_from*6:start_from*6+6]
    return render(request,"feed.html",context={"feed":announcements,"next":start_from+1,"bookmark":bookmarkcourses})

def about(request):
    stats   = Stat.objects.get(tag='initial')
    return render(request,"about.html",context={'stats':stats})

def _logout(request):
    logout(request)
    return redirect('home')

def forgetpassword(request):
    if request.method =='GET':
        form = ForgetPasswordForm()
        return render(request,"form.html",context={"form":form})
    elif request.method == 'POST':
        return render(request,"form.html",context={"message":"Check your email for password :)"})

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
        form = LoginForm()
        return render(request,"login.html",context={"form":form,"message":"forget password"})
        

def _register(request,register_as=None):
    if request.method =='GET':
        form = RegisterForm()
        return render(request,"register.html",context={"form":form})  
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if(register_as=='student'):
                user.user_role = 'student'
            elif(register_as=='instructor'):
                user.user_role = 'instructor'
            user.save()
            stat   = Stat.objects.get(tag='initial')
            stat.user_count +=1
            stat.save()
            return redirect(reverse('login'))
        return redirect(reverse('register',kwargs={"register_as":register_as}))
            
@login_required
def profile(request):
    if request.method == 'GET':
        email = request.GET.get('email',request.user)
        form = AvatorForm()
        owner = User.objects.get(email=email)
        is_owner = True if owner == request.user else False
        if  owner.user_role == "student":
            student,created = Student.objects.get_or_create(user=owner)
            return render(request,"profile.html",context={"user":request.user,"student":student,'form':form, 'is_owner':is_owner})        
        return render(request,"profile.html",context={"user":owner,'form':form, 'is_owner':is_owner})
    elif request.method =='POST':
        if 'name' in request.POST.keys():
            if request.POST['name'] in ['semester','registration_no','branch']:
                student = Student.objects.get(user=request.user)
                if request.POST['name'] == 'semester':
                    print('yeah')
                    student.semester = request.POST['value']
                elif request.POST['name'] == 'registration_no':
                    student.registration_no = request.POST['value']
                elif request.POST['name'] == 'branch':
                    student.branch = request.POST['value']
                student.save()
            elif request.POST['name'] in ['first_name','last_name']:
                user = User.objects.get(email = request.user.email)
                if request.POST['name'] == 'first_name':
                    user.first_name = request.POST['value']
                elif request.POST['name'] == 'last_name':
                    user.last_name = request.POST['value']
                user.save()
        else:
            user = User.objects.get(email=request.user.email)
            form = AvatorForm(request.POST,request.FILES)
            if form.is_valid():
                user.avatar = form.cleaned_data["avator"]
                user.save()
                print(user.avatar)
            print(form.errors)

        return redirect(reverse('profile'))
        # Profile edit to be implemented.

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


def Announcements(request,department=None,coursecode=None):
    if request.method =='GET':
        form= AnnouncementForm()
        return render(request,"form.html",context={"form":form})
    elif request.method =="POST":
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        form = AnnouncementForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj=Announcement()
            obj.files = form.cleaned_data["files"]
            obj.title = form.cleaned_data["title"]
            obj.description = form.cleaned_data["description"]
            obj.author=request.user
            obj.course= Course.objects.get(code=coursecode)
            obj.save()
            if created:
                stat   = Stat.objects.get(tag='initial')
                stat.contributor_count +=1
                stat.save()
            contributor,created = Contributor.objects.get_or_create(user=request.user)
            contributor.announcement +=1
            contributor.points += rewardvalue
            contributor.save()
            stat   = Stat.objects.get(tag='initial')
            stat.announcement_count +=1
            stat.save()
            return redirect(reverse("course", kwargs={'department':department,'coursecode':coursecode}))
        print(form.errors) 
        return redirect(reverse("course", kwargs={'department':department,'coursecode':coursecode}))

def Materials(request,department=None,coursecode=None):
    if request.method =='GET':
        form= MaterialForm()
        return render(request,"form.html",context={"form":form})
    elif request.method =="POST":
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        form = MaterialForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj = Material()
            obj.files = form.cleaned_data["files"]
            obj.title = form.cleaned_data["title"]
            obj.author=request.user
            obj.course= Course.objects.get(code=coursecode)
            obj.save()
            contributor,created = Contributor.objects.get_or_create(user=request.user)
            contributor.material +=1
            contributor.points += rewardvalue
            contributor.save()
            if created:
                stat   = Stat.objects.get(tag='initial')
                stat.contributor_count +=1
                stat.save()
            stat   = Stat.objects.get(tag='initial')
            stat.material_count +=1
            stat.save()
            return redirect(reverse("course", kwargs={'department':department,'coursecode':coursecode}))
        print(form.errors) 
        return redirect(reverse("course", kwargs={'department':department,'coursecode':coursecode}))

@login_required
def FeedbackView(request):
    if request.method =='GET':
        form= FeedbackForm()
        return render(request,"form.html",context={"form":form})
    elif request.method =="POST":
        form = FeedbackForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj = Feedback()
            obj.files = form.cleaned_data["files"]
            obj.title = form.cleaned_data["title"]
            obj.feedback = form.cleaned_data["feedback"]
            obj.author=request.user
            obj.save()
            contributor,created = Contributor.objects.get_or_create(user=request.user)
            contributor.feedback +=1
            contributor.points += 2*rewardvalue
            contributor.save()
            if created:
                stat   = Stat.objects.get(tag='initial')
                stat.contributor_count +=1
                stat.save()
            return render(request,"form.html",context={'feedback':True,'message':"Thanks for your valuable feedback. We will be working on your query."})
        print(form.errors) 
        return redirect(reverse("course"))


@login_required
def ExamPaperView(request,department=None,coursecode=None):
    if request.method =='GET':
        form= ExamPaperForm()
        return render(request,"form.html",context={"form":form})
    elif request.method =="POST":
        form = ExamPaperForm(request.POST,request.FILES)
        if(form.is_valid()):
            obj = ExamPaper()
            obj.files = form.cleaned_data["files"]
            obj.term = form.cleaned_data["term"]
            obj.author=request.user
            obj.course= Course.objects.get(code=coursecode)
            obj.save()
            contributor,created = Contributor.objects.get_or_create(user=request.user)
            contributor.paper +=1
            contributor.points += rewardvalue
            contributor.save()
            if created:
                stat   = Stat.objects.get(tag='initial')
                stat.contributor_count +=1
                stat.save()
            stat   = Stat.objects.get(tag='initial')
            stat.paper_count +=1
            stat.save()
            return redirect(reverse("course", kwargs={'department':department,'coursecode':coursecode}))
        print(form.errors) 
        return redirect(reverse("course", kwargs={'department':department,'coursecode':coursecode}))

def DepartmentView(request,department=None,year=0,semester=0):
    if request.method =='GET':
        dept     = get_object_or_404(Department,acronym=department)
        year     = int(year)
        semester = int(semester)
        if year < 1:
            # course = CourseAllotment.objects.select_related('course').filter(course__dept=dept).order_by('semester')
            return render(request,"years.html",context={'department':department})
        else:
            if semester == 0 :
                course = CourseAllotment.objects.select_related('course').filter(course__dept=dept).filter(semester__in=[(2*year -1),(2*year)])
                print(course)
            else:
                course = CourseAllotment.objects.select_related('course').filter(course__dept=dept).filter(semester=semester)

        return render(request,"department.html",context={"department":dept,"courses":course})


def CourseView(request,department=None,coursecode=None):
    if request.method =='GET':
        dept          = get_object_or_404(Department,acronym=department)
        course        = get_object_or_404(Course,code=coursecode)
        announcements = Announcement.objects.filter(course=course)
        materials     = Material.objects.filter(course=course)
        papers        = ExamPaper.objects.filter(course=course)
        try:
            bookmark  = Bookmark.objects.get(course=course,user=request.user)
        except:
            bookmark  = None
        is_bookmarked = True if bookmark else False   
        return render(request,"course.html",context={"department":dept,"course":course,"announcements":announcements,"materials":materials,"papers":papers,"is_bookmarked":is_bookmarked})
        
@login_required
def FeedView(request):
    if request.method=='GET':
        bookmarks  =Bookmark.objects.filter(user=request.user)
        bookmarkcourses = Bookmark.objects.select_related('course').filter(user=request.user)
        courselist=[]
        for bookmark in bookmarks:
            courselist.append(bookmark.course)
        start_from = int(request.GET.get('start_from',0))
        announcements = Announcement.objects.select_related('author').filter(course__in =courselist ).order_by('-updated_on')[start_from*6:start_from*6+6]
        return render(request,"feed.html",context={"feed":announcements,"next":start_from+1})

@login_required
def BookmarkView(request):
    if request.method =='POST':
        course     = request.POST.get('course')
        user       = request.POST.get('user')
        course_obj = get_object_or_404(Course,id=course)
        try:
            bookmark  = Bookmark.objects.get(course=course,user=request.user)
        except:
            bookmark  = None
        if bookmark is not None:
            bookmark.delete()
        else:
            obj        = Bookmark()
            obj.course = course_obj
            obj.user   = request.user
            obj.save()
        return HttpResponse(json.dumps({"success":True}),content_type='application/json')

