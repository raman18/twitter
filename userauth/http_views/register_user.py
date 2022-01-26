from logging import Logger
import json
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.views import BaseView, get_hashed_password, require_auth
from userauth.model.access_token_model import AccessToken
from userauth.models import User


class RegisterUser(BaseView):
    def post(self, request):
        json_data = json.loads(request.body)

        user_exists = User.objects.filter(email=json_data["email"])
        if user_exists:
            return HttpResponse("You are already registered with us.")
        else:
            user = User()
            user.name = json_data["name"]
            user.email = json_data["email"]
            user.username = json_data["username"]
            user.password = get_hashed_password(json_data["password"])
            user.save()
            user_access_token = AccessToken()
            user_access_token.user = user
            user_access_token.access_token = AccessToken.generate()
            user_access_token.save()
            return HttpResponse("User name is " + user.name + " and token is " + user_access_token.access_token)
        return HttpResponse("You can register user here.")
    
    @require_auth
    def update(self, request):
        json_data = json.loads(request.body)
        print(request.subject)
        user_exists = User.objects.filter(username=json_data["username"])
        if user_exists:
            return HttpResponse("Choose other username.")
        else:
            user = User()
            user.name = json_data["name"]
            user.email = json_data["email"]
            user.username = json_data["username"]
            user.password = get_hashed_password(json_data["password"])
            user.save()
            return HttpResponse("User registered.")
        return HttpResponse("You can register user here.")