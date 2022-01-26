from django.urls import path
from . import views


urlpatterns = [
    path("user", views.RegisterUser.as_view(), name="user"),
    path("auth", views.LoginLogout.as_view(), name="auth"),
]
