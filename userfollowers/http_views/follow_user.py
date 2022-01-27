import json
from logging import Logger
from django.shortcuts import redirect
from django.http import HttpResponse
from common.i18n import translate as _
from userauth.models import User
from userfollowers.models import UserFollower
from common.views import BaseView, require_auth


class FollowUserView(BaseView):
    @require_auth
    def post(self, request):
        json_data = json.loads(request.body)
        print("user in follow user request is")
        print(request.user)
        print(request.token)
        if request.user.user_id == json_data["followee"]:
            return self.build_response(
                None,
                code=422,
                message="You cannot follow yourself.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        followee_detail = User.objects.filter(user_id = json_data["followee"]).first()
        if not followee_detail:
            return self.build_response(
                None,
                code=401,
                message="Followee details not found.",
                localized_message=_("USER_NOT_FOUND"),
            )

        user_followers = UserFollower.objects.filter(user = request.user.user_id, follower= json_data["followee"]).first()
        if user_followers:
            return self.build_response(
                None,
                code=200,
                message="You are already following " + followee_detail.name,
                localized_message=_("USER_NOT_FOUND"),
            )
        
        follow = UserFollower()
        print(follow)
        follow.user = request.user
        follow.follower = followee_detail
        follow.save()
        return self.build_response(
                None,
                code=201,
                message="Now you are already following " + followee_detail.name,
                localized_message=_("STARTED_FOLLOWING"),
            )