from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home,name="home"),
    url(r'login',views._login,name="login"),
    url(r'logout',views._logout,name="logout"),
    url(r'register',views._register,name="register"),
]
