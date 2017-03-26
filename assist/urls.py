from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'^about$', views.about,name="about"),
    url(r'^login$',views._login,name="login"),
    url(r'^logout$',views._logout,name="logout"),
    url(r'^feed$',views.FeedView,name="feed"),
    url(r'^feedback',views.FeedbackView,name="feedback"),
    url(r'^bookmark$',views.BookmarkView,name="bookmark"),
    url(r'^register/(?P<register_as>\w+)',views._register,name="register"),
    url(r'^profile$',views.profile,name="profile"), 
    url(r'^feed',views.FeedView,name="feed"),
    url(r'^forgetpassword$',views.forgetpassword,name="forgetpassword"),
    url(r'^(?P<department>\w+)/(?P<coursecode>\w+)/announcements$',views.Announcements,name="announcements"),
    url(r'^(?P<department>\w+)/(?P<coursecode>\w+)/material$',views.Materials,name="material"),
    url(r'^(?P<department>\w+)/(?P<coursecode>\w+)/exampaper$',views.ExamPaperView,name="exampaper"),
    url(r'^services/getdepartments.json$',views.getDepartments,name="getdepartments"),
    url(r'^services/(?P<department>\w+)/getcourses.json$',views.getCourses,name="getcourses"),
    url(r'^department/(?P<department>\w+)/(?P<year>[0-5])/(?P<semester>([0-9]|10)$)$',views.DepartmentView,name="department"),  
    url(r'^(?P<department>\w+)/(?P<coursecode>\w+)',views.CourseView,name="course"),

    
]
 