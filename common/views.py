from django.shortcuts import render
# import bcrypt
import json
from django.http import HttpRequest, HttpResponse
from django.views.generic import View

class BaseView(View):
    def http_method_not_allowed(self, request, *args, **kwargs):
        status = {}
        status["status"] = 405
        status["message"] = "Method Not Allowed"
        status["localized_message"] = _("PROBLEM_REPORTED")
        status["success"] = False
        data = {"status": status}
        response = super().http_method_not_allowed(request, args, kwargs)
        response.content = json.dumps(data)
        response["content-type"] = "application/json"
        return response

    @staticmethod
    def build_response(
        body,
        headers=None,
        code=200,
        message="OK",
        # localized_message=_("DONE"),
        localized_message = "DONE",
        success=True,
    ):
        status = {}
        status["status"] = code
        status["message"] = message
        status["localized_message"] = localized_message
        status["success"] = success
        response = {"status": status}
        if body is not None:
            response["response"] = body
        response = HttpResponse(
            json.dumps(response), status=code, content_type="application/json"
        )
        if headers:
            for key, val in headers.items():
                response.__setitem__(key, val)
        return response

def get_hashed_password(plain_text_password):
    return "bcrypt"
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

def check_password(plain_text_password, hashed_password):
    return "bcrypt"
    return bcrypt.checkpw(plain_text_password, hashed_password)