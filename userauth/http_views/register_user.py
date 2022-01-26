from logging import Logger
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt
from common.views import BaseView, get_hashed_password
from userauth.models import User


class RegisterUser(BaseView):
    def post(request):
        print(request.body)
        user = User()
        user_exists = user.objects.filter(email=request.body.email)
        if user_exists:
            return HttpResponse("You are already registered with us.")
        else:
            user.name = request.body.name
            user.email = request.body.email
            user.username = request.body.username
            user.password = get_hashed_password(request.body.password)
            user.save()
            return HttpResponse("User registered.")
        return HttpResponse("You can register user here.")