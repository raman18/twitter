from logging import Logger
import json
from os import access
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.i18n import translate as _
from common.views import BaseView, get_hashed_password,check_password, require_auth
from userauth.model.access_token_model import AccessToken
from userauth.models import User


class RegisterUser(BaseView):
    def post(self, request):
        json_data = json.loads(request.body)

        if not "name" in json_data:
            return self.build_response(
                None,
                code=422,
                message="Name is required.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if not "email" in json_data:
            return self.build_response(
                None,
                code=422,
                message="Email is required.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if not "username" in json_data:
            return self.build_response(
                None,
                code=422,
                message="Username is required.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if not "password" in json_data:
            return self.build_response(
                None,
                code=422,
                message="Password is required.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )

        json_data["username"].replace(" ", "")
        
        if(len(json_data["username"]) > 20):
            return self.build_response(
                None,
                code=422,
                message="Choose a username of length 5 to 20.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if(len(json_data["username"]) < 5):
            return self.build_response(
                None,
                code=422,
                message="Choose a username of length 5 to 20.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if(len(json_data["password"]) > 20):
            return self.build_response(
                None,
                code=422,
                message="Choose a password of length 5 to 20.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if(len(json_data["password"]) < 5):
            return self.build_response(
                None,
                code=422,
                message="Choose a password of length 5 to 20.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if(len(json_data["name"]) > 50):
            return self.build_response(
                None,
                code=422,
                message="Choose a name of length 5 to 20.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if(len(json_data["name"]) < 5):
            return self.build_response(
                None,
                code=422,
                message="Choose a name of length 5 to 50.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )

        if(len(json_data["email"]) > 20):
            return self.build_response(
                None,
                code=422,
                message="Choose a email of length 5 to 50.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )
        
        if(len(json_data["email"]) < 5):
            return self.build_response(
                None,
                code=422,
                message="Choose a email of length 5 to 20.",
                localized_message=_("UNPROCESSABLE_ENTITY"),
            )

        username_exists = User.objects.filter(username=json_data["username"])
        if username_exists:
            return self.build_response(
                None,
                code=422,
                message="Choose other username.",
                localized_message=_("USERNAME_NOT_AVAILABLE"),
            )

        user_exists = User.objects.filter(email=json_data["email"])
        if user_exists:
            return self.build_response(
                None,
                code=422,
                message="Email is already regietered with us.",
                localized_message=_("USER_ALREADY_REGISTERED"),
            )
        else:
            user = User()
            user.name = json_data["name"]
            user.email = json_data["email"]
            user.username = json_data["username"]
            user.password = (get_hashed_password(json_data["password"].encode("utf-8"))).decode("utf-8")
            user.save()
            user_access_token = AccessToken()
            user_access_token.user = user
            user_access_token.access_token = AccessToken.generate()
            user_access_token.save()
            result = [{"access_token": user_access_token.access_token}]
            return self.build_response(
                result,
                code=201,
                message="User created.",
                localized_message=_("USER_CREATED"),
            )