import json
from logging import Logger
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.views import BaseView, get_hashed_password
from followers.models import Followers
from updates.models import Update
from userauth.models import User


class TimeLineView(BaseView):
    def get(self, request):
        print("Get Feeds")
        json_data = json.loads(request.body)
        user_followers = Followers.objects.filter(user = json_data["user"]).only('follower')
        print("user followers are")
        print(user_followers)
        if user_followers:
            users = []
            for user in user_followers.iterator():
                users.append(user.follower)
        print(users)
        timeline = Update.objects.filter(user__in = users).only('update_id','content',).order_by('-update_id').all()
        if not timeline:
            return HttpResponse("Follow some users.")
        else:
            return HttpResponse(timeline)
        return HttpResponse("You can register user here.")