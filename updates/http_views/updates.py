from logging import Logger
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.views import BaseView, get_hashed_password
from updates.models import Update
from userauth.models import User


class UpdateView(BaseView):
    def post(self, request):
        print("test create post")
        json_data = json.loads(request.body)
        user_detail = User.objects.filter(user_id = json_data["user"]).first()
        
        if not user_detail:
            return HttpResponse("User not found.")
        
        if(len(json_data["content"]) > 140):
            return HttpResponse("Post content length exceeded.")
        
        update = Update()
        update.user_id =json_data["user"]
        update.content = json_data["content"]
        update.save()
        return HttpResponse("Post Created.")