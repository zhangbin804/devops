import time
from apps.permissions import models as permissions_models
from apps.accounts.forms.forms import CreateUserForm,CreateRolesForm,ChangeUserForm


def create_edit_user(request,use='create'):
    user_dict = {}
    if use == 'create':
        user_dict['create_time'] = time.strftime('%Y-%m-%d %X')
        user_dict['name'] = request.POST.get('user')
    user_dict['username'] = request.POST.get('username', '')
    user_dict['email'] = request.POST.get('email')
    password = request.POST.get('password', '')
    if password:
        user_dict['password'] = password
    if not user_dict['username']:
        del user_dict['username']
    if not user_dict['email']:
        del user_dict['email']
    disable = request.POST.get('disable', '')
    if disable:
        disable = 0
    else:
        disable = 1
    user_dict['disable'] = disable
    return user_dict
