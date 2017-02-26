from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'(?P<coursecode>\w+)/announcements$',views.Announcements,name="announcements"),
    url(r'(?P<coursecode>\w+)/material$',views.Materials,name="material"),
    url(r'(?P<coursecode>\w+)/exampaper$',views.ExamPapers,name="exampaper"),

]
 