from django.shortcuts import redirect
from apps.permissions.models import User

def auth(func):
    def inner(request, *args, **kwargs):
        is_login = request.session.get('is_login', False)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('/login/')
    return inner


def get_user_id(user):
    user_id = User.objects.get(name=user).id
    return user_id

