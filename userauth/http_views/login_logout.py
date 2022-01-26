from logging import Logger
import json
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, logout
from common.views import BaseView, check_password, require_auth
from userauth.models import User


class LoginLogout(BaseView):
    @require_auth
    def post(self, request):
        json_data = json.loads(request.body)
    
        user_exists = User.objects.filter(username=json_data["username"]).first()
        print("user password is")
        if not user_exists:
            return HttpResponse("Username is wrong.")
        else:
            if check_password(json_data["password"], user_exists.password):
                return HttpResponse("User is authorized.")
            else:
                return HttpResponse("Password is wrong.")

    @require_auth
    def delete(request):
        logout(request)
        Logger.info(request, "Logged out successfully!")
        return redirect("main:homepage")