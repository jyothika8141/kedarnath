from django.urls import re_path as url

from main.auth import auth
from main import views

urlpatterns = [
    url(r'^logout/$', auth.logout, name="logout"),
    url(r'^login/$', auth.login, name="login"),
    url(r'^check/in/$', views.check_in, name="signup"),
    url(r'^check/out/$', views.check_out, name="signup"),
    url(r'^attendance/status/$', views.check_attendance, name="signup"),
    url(r'^leave/request/$', views.submit_leave_request, name="signup"),
    url(r'^leave/requests/$', views.get_leave_requests, name="signup"),
]