from django.conf.urls import url
from . import views

urlpatterns = [
    url('register', views.AccountRegister.as_view()),
    url('login', views.AccountLogin.as_view()),
    url('logout', views.AccountLogout.as_view())
]