from django.urls import path
from . import views

urlpatterns = [
    path("post", views.UserPostView.as_view(), name="post"),
    path("feeds", views.UserFeedsView.as_view(), name="feeds"),
]
