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
        if request.user.user_id == int(json_data["follower"]):
            return self.build_response(
                None,
                code=422,
                message="You cannot follow yourself.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        follower_detail = User.objects.filter(user_id = json_data["follower"]).first()
        if not follower_detail:
            return self.build_response(
                None,
                code=401,
                message="Follower details not found.",
                localized_message=_("USER_NOT_FOUND"),
            )

        user_followers = UserFollower.objects.filter(user = request.user.user_id, follower= json_data["follower"]).first()
        if user_followers:
            return self.build_response(
                None,
                code=200,
                message="You are already following " + follower_detail.name,
                localized_message=_("ALREADY_FOLLOWING"),
            )
        
        follow = UserFollower()
        follow.user = request.user
        follow.follower = follower_detail
        follow.save()
        return self.build_response(
                None,
                code=201,
                message="Now you are following " + follower_detail.name,
                localized_message=_("STARTED_FOLLOWING"),
            )