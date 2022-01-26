from logging import Logger
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from userauth.models import User
from followers.models import Followers
from common.views import BaseView


class SuggestionView(BaseView):
    def get(self,request):
        print(request.GET.get("user"))
        print("suggest user ")
        inner_qs = Followers.objects.filter(user = request.GET.get("user"))
        suggestions = User.objects.exclude(user_id__in=inner_qs).all()
        if not suggestions:
            return HttpResponse("No suggestions list.")
        else:
            return HttpResponse(suggestions)