from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'login',views._login,name="login"),
    url(r'logout',views._logout,name="logout"),
    url(r'register',views._register,name="register"),
    url(r'profile',views.profile,name="profile"),
    url(r'(?P<coursecode>\w+)/announcements$',views.Announcements,name="announcements"),
    url(r'(?P<coursecode>\w+)/material$',views.Materials,name="material"),
    url(r'(?P<coursecode>\w+)/exampaper$',views.ExamPapers,name="exampaper"),
    url(r'services/getdepartments.json$',views.getDepartments,name="getdepartments"),
    url(r'services/(?P<department>\w+)/getcourses.json$',views.getCourses,name="getcourses"),
    url(r'department/(?P<department>\w+)/',views.DepartmentView,name="department")
]
 