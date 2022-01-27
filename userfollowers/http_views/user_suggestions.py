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
        print("suggest user ")
        print(request.user.user_id)
        request.user.user_id = 1
        print(request.token)
        inner_qs = UserFollower.objects.filter(user = request.user.user_id).values('follower')
        suggestions = User.objects.exclude(user_id__in=inner_qs).all()
        print(suggestions)
        suggestions1 = User.objects.exclude(user_id__in=inner_qs)
        print("query is")
        print(suggestions1.query)

        if suggestions:
            result = []
            for user in suggestions.iterator():
                if user.user_id == request.user.user_id:
                    continue
                result.append({user.user_id: user.name})
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