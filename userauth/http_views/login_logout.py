from logging import Logger
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import login, logout
from common.views import BaseView, check_password
from userauth.models import User


class LoginLogout(BaseView):
    @csrf_exempt
    def post(request):
        print(request.body)
        user = User()
        user_exists = user.objects.filter(username=request.body.username)
        if not user_exists:
            return HttpResponse("You are not registered with us.")
        else:
            if check_password(request.body.email.password, user_exists.password):
                login(request, user)
                return HttpResponse("User is authorized.")
        return HttpResponse("You can register user here.")

    @csrf_exempt
    def delete(request):
        logout(request)
        Logger.info(request, "Logged out successfully!")
        return redirect("main:homepage")