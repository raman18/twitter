from django.urls import path
from . import views

urlpatterns = [
    path("update", views.UpdateView.as_view(), name="update"),
    path("timelines", views.TimeLineView.as_view(), name="timelines"),
]
