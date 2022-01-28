from logging import Logger
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.views import BaseView, get_hashed_password, require_auth
from userposts.models import UserPost
from common.i18n import translate as _
from userauth.models import User


class UserPostView(BaseView):
    @require_auth
    def post(self, request):
        json_data = json.loads(request.body)

        if not "content" in json_data:
            return self.build_response(
            None,
            code=422,
            message="Content is required.",
            localized_message=_("UNPROCESSABLE_ENTITY"),
        )

        if(len(json_data["content"]) == 0):
            return self.build_response(
            None,
            code=422,
            message="Content is empty.",
            localized_message=_("UNPROCESSABLE_ENTITY"),
        )
        
        if(len(json_data["content"]) > 140):
            return self.build_response(
                None,
                code=422,
                message="Content length exceeded.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        user_post = UserPost()
        user_post.user_id = request.user.user_id
        user_post.content = json_data["content"]
        user_post.save()
        return self.build_response(
            None,
            code=201,
            message="Created",
            localized_message=_("POST_CREATED"),
        )