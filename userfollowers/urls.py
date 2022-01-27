from django.urls import path
from . import views


urlpatterns = [
    path('follow_user', views.FollowUserView.as_view(), name='follow_user'),
    path('user_suggestions', views.UserSuggestionView.as_view(), name='user_suggestions'),
]