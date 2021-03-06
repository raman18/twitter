import logging
import json
from datetime import datetime
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from pytz import timezone
import pytz
from common.i18n import translate as _
from django.contrib.auth import login, logout
from common.views import BaseView, check_password, get_hashed_password, require_auth
from userauth.model.access_token_model import AccessToken
from userauth.models import User

logger = logging.getLogger(__name__)

class LoginLogout(BaseView):
    
    def post(self, request):
        logger.info("Handling login call.")
        json_data = json.loads(request.body)

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

        user = User.objects.filter(username=json_data["username"]).first()
        if not user:
            return self.build_response(
                None,
                code=201,
                message="Wrong username",
                localized_message=_("USERNAME_NOT_FOUND"),
            )
        else:
            if check_password(json_data["password"].encode("utf-8"), user.password.encode("utf-8")):
                user_access_token = AccessToken()
                user_access_token.user = user
                user_access_token.access_token = AccessToken.generate()
                user_access_token.save()
                result = [{"access_token": user_access_token.access_token}]
                return self.build_response(
                    result,
                    code=200,
                    message="You are logged in successfully.",
                    localized_message=_("LOGIN_OK"),
                )
            else:
                return self.build_response(
                    None,
                    code=422,
                    message="Entered wrong password.",
                    localized_message=_("WRONG_LOGIN_PASSWORD"),
                )

    @require_auth
    def delete(self, request):
        logger.info("Handling logout call.")
        if request.token:
            request.token.expires_at = datetime.now(pytz.utc)
            request.token.save()

        return self.build_response(
            None, 
            code=200, 
            message="You are logged out successfully.", 
            localized_message=_("LOGOUT_OK")
        )