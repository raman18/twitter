import json
from logging import Logger
from unittest import result
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.i18n import translate as _
from common.views import BaseView, get_hashed_password, require_auth
from userfollowers.models import UserFollower
from userposts.models import UserPost
from userauth.models import User


class UserFeedsView(BaseView):
    @require_auth
    def get(self, request):
        user_followers = UserFollower.objects.filter(user = request.user).only('follower')
        if user_followers:
            users = []
            for user in user_followers.iterator():
                users.append(user.follower)
        else:
            return self.build_response(
                None,
                code=200,
                message="Follow some people.",
                localized_message=_("NOT_FOLLOWING_ANYONE"),
            )

        timeline = UserPost.objects.filter(user__in = users).only('post_id','content',).order_by('-created_at').all()
        
        if timeline:
            result = []
            for feed in timeline.iterator():
                result.append({"name": feed.user.name, "created_at": str(feed.created_at), "post_id": feed.post_id, "content" : feed.content})

            return self.build_response(
                result,
                code=200,
                message="Success",
                localized_message=_("FEEDS_FOUND"),
            )
        else:
            return self.build_response(
                None,
                code=200,
                message="Feeds not found.",
                localized_message=_("FEEDS_NOT_FOUND"),
            )