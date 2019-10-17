from django import template
from django.utils.safestring import mark_safe
from apps.operational.models import *

register = template.Library()

@register.simple_tag
def is_radio_checked(value):
    if value:
        return 'checked'

@register.simple_tag
def class_server_auth(value):
    if not value:
        return 'server_auth'

@register.simple_tag
def get_ssh_user_value(value):
    if value:
        return value
    else:
        return ''

@register.simple_tag
def get_ssh_password_value(value):
    if value:
        return '******'
    else:
        return ''

@register.simple_tag
def get_group_server(value):
    if value:
        server_list = str(value).split('|')
        ret = ''
        for i in server_list:
            server_id = Server.objects.filter(server_name=i).values('id')[0]['id']
            server_href = '/operational/read/server/%s/'%(server_id)
            i = '<a href="%s" style="color: blue;">%s</a>'%(server_href,i)
            if ret:
                ret = ret+'&nbsp;'+i
            else:
                ret = i
        return mark_safe(ret)
    return ''


@register.simple_tag
def get_server_user_way(value):
    if not value:
        return ''
    elif value == 1:
        return '服务器'
    elif value == 2:
        return '服务器组'

@register.simple_tag
def get_server_user_way_list(way,id):
    if not way:
        return ''
    elif way == 1:
        html = '''
        <a href="/operational/read/server/{href}/" style="color:blue; font-size: 18px;">{server_name}</a> &nbsp;
        '''
        ret = ''
        server = ServerUser.objects.get(id=id).servers.all()
        for i in server:
            i = html.format(href=i.id,server_name=i.server_name)
            if ret:
                ret = ret + i
            else:
                ret = i
        return mark_safe(ret)
    elif way == 2:
        html = '''
               <a href="/operational/read/group/{href}/" style="color:blue; font-size: 18px;">{server_name}</a> &nbsp;
               '''
        ret = ''
        server = ServerUser.objects.get(id=id).groups.all()
        for i in server:
            i = html.format(href=i.id, server_name=i.title)
            if ret:
                ret = ret + i
            else:
                ret = i
        return mark_safe(ret)


