from django.urls import path
from . import views


urlpatterns = [
    path('follow', views.FollowView.as_view(), name='follow'),
    path('suggestions', views.SuggestionView.as_view(), name='suggestions'),
]