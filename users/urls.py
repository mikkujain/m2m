from django.conf.urls import url
from django.contrib import admin
import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^$', views.Home, name="name"),
    url(r'^$', auth_views.login, {"template_name": "home.html", "redirect_authenticated_user": True}, name="login"),
    url(r'^logout/$', auth_views.logout,  {'next_page': '/'}, name="logout"),
    url(r'^dashboard/$', views.Dashboard.as_view(), name="dashboard"),
]