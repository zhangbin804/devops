from django import template
from django.utils.safestring import mark_safe
from apps.permissions.models import User
from apps.process.models import Intermediate,Process
from apps.accounts.core.accounts_auth import get_user_id

register = template.Library()



@register.simple_tag
def getUser(id):
    user_obj = User.objects.filter(id=id)
    return user_obj


@register.simple_tag
def isOption(value,session_value):
    if value == session_value:
        return 'selected'
    else:
        return ''


@register.simple_tag
def getStatus(status):
    if status == '0':
        return mark_safe('<span style="color: chocolate;">审核中</span>')
    elif status == '1':
        return mark_safe('<span style="color: red;">审核拒绝</span>')
    elif status == '2':
        return mark_safe('<span style="color: green;">审核通过</span>')




@register.simple_tag
def getDescreba(user_id,intermediate_id,process_str):
    intermediate_obj = Intermediate.objects.filter(id=int(intermediate_id))
    user = intermediate_obj.values('user')[0]['user']
    status = intermediate_obj.values('status')[0]['status']
    process_srt_list = process_str.split(',')
    # if str(user_id) in process_srt_list:
    user_index = process_srt_list.index(str(user_id))
    process_user_index =  process_srt_list.index(user)
    if status == '2':
        return mark_safe('<span style="color: green;">审核通过</span>')
    elif status == '0' and user_index < process_user_index:
        return mark_safe('<span style="color: green;">审核通过</span>')
    elif status == '0' and  process_user_index == user_index:
        return mark_safe('<span style="color: chocolate;">审核中</span>')
    elif status == '1' and process_user_index > user_index:
        return mark_safe('<span style="color: green;">审核通过</span>')
    elif status == '1' and process_user_index == user_index:
        return mark_safe('<span style="color: red;">审核拒绝</span>')
    else:
        return mark_safe('<span></span>')



@register.simple_tag
def get_messages(user):
    html_a = '''
        <a href="/process/audit/info/?audit={id}">
            <span class="image"><img src="/{avatar}" alt="Profile Image" />{username}</span>
                <span>
                <span></span>
                <span class="time"></span>
                </span>
            <span class="message">
                待审核流程: {process_name}
            </span>
        </a>
        
        '''
    user_id = get_user_id(user)
    process_user_all = Intermediate.objects.filter(user=user_id,is_read=0,status=0).all()
    message = ''
    for i in process_user_all:
        # id = i.id
        # avatar = i.create_user.head_img
        # username = i.create_user.username
        # process_name = i.name
        i = html_a.format(id=i.id,avatar=i.create_user.head_img,username=i.create_user.username,process_name=i.name)
        if message:
            message += i
        else:
            message = i

    return mark_safe(message)




@register.simple_tag
def count_process(user):
    user_id = get_user_id(user)
    process_user_all_count = Intermediate.objects.filter(user=user_id, is_read=0, status=0).all().count()
    if not process_user_all_count:
        return ''
    return process_user_all_count


@register.simple_tag
def get_attachment(attachment):
    html_a = '<a href="/{href}" style="color: blue;" download="{file_name}">下载附件</a>'
    if attachment:
        file_name = str(attachment).split('/')[-1]
        ret = html_a.format(href=attachment,file_name=file_name)
        return mark_safe(ret)
    return ''

