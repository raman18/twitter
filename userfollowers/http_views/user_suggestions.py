from logging import Logger
from django.shortcuts import redirect
from django.http import HttpResponse
from common.i18n import translate as _
from userauth.models import User
from userfollowers.models import UserFollower
from common.views import BaseView, require_auth


class UserSuggestionView(BaseView):
    @require_auth
    def get(self,request):
        inner_qs = UserFollower.objects.filter(user = request.user.user_id).values('follower')
        suggestions = User.objects.exclude(user_id__in=inner_qs).all()
        suggestions1 = User.objects.exclude(user_id__in=inner_qs)

        if suggestions:
            result = []
            for user in suggestions.iterator():
                if user.user_id == request.user.user_id:
                    continue
                result.append({"user_id" :user.user_id, "name": user.name})
            return self.build_response(
                result,
                code=200,
                message="Follow some people.",
                localized_message=_("SUGGESTIONS_FOUND"),
            )
        else:
            return self.build_response(
                None,
                code=204,
                message="No Suggestions found.",
                localized_message=_("SUGGESTIONS_NOT_FOUND"),
            )