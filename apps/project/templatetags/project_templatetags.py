from django import template
from django.utils.safestring import mark_safe
from apps.project.models import *

register = template.Library()

@register.simple_tag
def get_git_auth_way(v1,v2):
    if v1 == v2:
        return 'checked="checked"'
    else:
        return ''
@register.simple_tag
def show_default_auth(v1,v2):
    if v1 == v2:
        return ''
    else:
        return 'server_auth'

@register.simple_tag
def connection_status(value):
    if value == 0:
        return mark_safe('<span style="color: chocolate; font-size: 30px">●</span>')
    elif value == 1:
        return mark_safe('<span style="color: red;font-size: 30px">●</span>')
    elif value == 2:
        return mark_safe('<span style="color: green;font-size: 30px">●</span>')

@register.simple_tag
def get_tag(log_id):
    if log_id:
        tag = Log.objects.get(id=log_id).git_tag
        return tag
    return ''

@register.simple_tag
def get_new_time(log_id):
    if log_id:
        new_time = Log.objects.get(id=log_id).new_time
        return new_time
    return ''


# @register.simple_tag
# def show_default_select(v1,v2):
#     if v1 == v2:
#         return 'selected'
#     else:
#         return ''
