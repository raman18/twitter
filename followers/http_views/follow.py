import json
from logging import Logger
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from userauth.models import User
from followers.models import Followers
from common.views import BaseView, require_auth


class FollowView(BaseView):
    @require_auth
    def post(self, request):
        json_data = json.loads(request.body)
        print("user in follow user request is")
        print(request)
        if json_data["user"] == json_data["followee"]:
            return HttpResponse("Insufficient data.")
        
        followee_detail = User.objects.filter(user_id = json_data["followee"]).first()
        if not followee_detail:
            return HttpResponse("Followee not found.")
        
        user_detail = User.objects.filter(user_id = json_data["user"]).first()
        if not user_detail:
            return HttpResponse("User not found.")

        user_followers = Followers.objects.filter(user = json_data["user"], follower= json_data["followee"]).first()
        if user_followers:
            return HttpResponse("You already follow " + followee_detail.name)
        
        
        follow = Followers()
        print("follower object is")
        print(follow)
        follow.user = user_detail
        follow.follower = followee_detail
        follow.save()
        return HttpResponse("Now you are following " + followee_detail.name)