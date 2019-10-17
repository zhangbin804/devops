from django import forms
import re
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def special_auth(value):
    special_re = re.findall(r'[\'\"\\#;!~`\*<>\[\]\(\)\?]',value)
    if special_re:
        raise ValidationError('输入非法字符')

def sql_auth(value):
    sql_re = re.findall(r'[#\'\"\(\)/*]',value)
    if sql_re:
        raise ValidationError('输入非法字符')

def user_auth(value):
    user_re = re.compile(r'^[a-zA-Z_][0-9a-zA-Z_]+')
    if not user_re.match(value):
        raise ValidationError('输入格式错误')

def password_auth(value):
    passowrd_re = re.findall(r'[|#&\\\'\" ]',value)
    if passowrd_re:
        raise ValidationError('输入非法字符')



def is_digital(value):
    digital_re = re.findall(r'[0-9]+',str(value))
    if not digital_re:
        raise ValidationError('输入格式错误')

def is_ip(value):
    ip_re = re.compile('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    if not ip_re.match(value):
        raise ValidationError('输入格式错误')

def sudo_auth(value):
    sudo_re = re.findall(r'[|# ;&?\'"]', value)
    if sudo_re:
        raise ValidationError('输入非法字符')

def ugid_auth(value):
    if value < 1000 or value >60000:
        raise ValidationError('输入范围不允许')




class LoginUserForm(forms.Form):
    username = forms.CharField(label='账 号',max_length=32,error_messages={'required': '账号不能为空'},
                               validators=[user_auth,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'账 号','required':''}))
    password = forms.CharField(label='密 码', min_length=6,max_length=64,error_messages={'required': '密码不能为空','invalid': u'请输入有效邮箱'},
                               validators=[password_auth,],
                               widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'密 码','required':'', 'min_length': '密码长度不能小于6'}))

    # password =  forms.ChoiceField(widget = forms.Select(),
    #                  choices = ([('1','1'), ('2','2'),('3','3'), ]), initial='3', required = True,)
    # password = forms.ChoiceField(widget=forms.RadioSelect,choices=(('1', '男',), ('2', '女',)),initial='1')
class AddUserForm(forms.Form):
    username = forms.CharField(label='账 号',max_length=32, error_messages={'required': '账号不能为空'},
                               validators=[user_auth,],
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '账 号', 'required': ''}))

    user = forms.CharField(label='姓 名',max_length=32, error_messages={'required': '姓名不能为空'},
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '姓名', 'required': ''}))

    password = forms.CharField(label='密 码', min_length=6, max_length=64, error_messages={'required': '密码不能为空'},
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': '密 码', 'required': '',
                                          'min_length': '密码长度不能小于6'}))

    email = forms.CharField(label='邮 箱',min_length=6, max_length=64,error_messages={'required': '邮箱不能为空', 'min_length': '密长度不能小于6', 'max_length': '长度不能大于64', },
                            widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '原密码', 'required': ''}))

    # gender = forms.ChoiceField(label='性 别',widget=forms.RadioSelect,choices=(('1', '男',), ('2', '女',)),initial='1')
    #
    #

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='旧密码',min_length=6, max_length=32,
                                   error_messages={'required': '密码不能为空', 'min_length': '密码长度不能小于6',
                                                   'max_length': '密码长度不能大于32', },
                                   widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'原密码','required':''}))

    new_password = forms.CharField(label='新密码',min_length=6, max_length=32,
                                   error_messages={'required': '密码不能为空', 'min_length': '密码长度不能小于6','max_length': '密码长度不能大于32', },
    widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '新密码', 'required': ''}))

    new_password2 = forms.CharField(label='新密码2',min_length=6, max_length=32,
                                    error_messages={'required': '密码不能为空', 'min_length': '密码长度不能小于6',
                                                    'max_length': '密码长度不能大于32', },
    widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '重复新密码', 'required': ''}))



class ChangeEmailForm(forms.Form):
    email = forms.CharField(label='邮 箱',min_length=6,max_length=64,
                                error_messages={'required': '邮箱不能为空', 'min_length': '密长度不能小于6',
                                                'max_length': '长度不能大于64', },
                                widget=forms.EmailInput(
                                    attrs={'class': 'form-control', 'placeholder': '新邮箱', 'required': ''}))


class ProcessName(forms.Form):
    process_name = forms.CharField(label="项目流程名",min_length=1,max_length=64,
                                   error_messages={'required': '项目流程名不能为空', 'min_length': '长度不能小于1',
                                                   'max_length': '长度不能大于64', },
                                   widget=forms.TextInput(attrs={'class':'form-control','name':'process_name','placeholder':''})
                                   )


class CreateUserProcessForm(forms.Form):
    create_name = forms.CharField(label='创建的流程名',max_length=32, error_messages={'required': '不能为空'},
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '流程名', 'required': '','name':'create_name'}))


class EditAvatar(forms.Form):
    avatar = forms.CharField(label='头 像',error_messages={'required': '不能为空'},widget=forms.FileInput(
        attrs={'id':'img_input','name':'avatar','accept':'image/*'}
    ))


class CreateUserForm(forms.Form):
    user = forms.CharField(label='账 号',max_length=32,error_messages={'required': '账号不能为空'},
                           validators=[user_auth,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','required':'','name':'user'}))
    username = forms.CharField(label='姓名',max_length=32,error_messages={'required': '不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','required':'','name':'username'}))
    email = forms.CharField(label='邮 箱',min_length=6,max_length=64,
                                error_messages={'required': '邮箱不能为空', 'min_length': '密长度不能小于6',
                                                'max_length': '长度不能大于64', },
                                widget=forms.EmailInput(
                                    attrs={'class': 'form-control', 'name':'email','placeholder': '', 'required': ''}))
    password = forms.CharField(label='密 码', min_length=6, max_length=64, error_messages={'required': '密码不能为空'},
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': '', 'required': '','name':'password'}))


class CreateRolesForm(forms.Form):
    role = forms.CharField(label='角色组',max_length=32,error_messages={'required': '不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','required':'','name':'role'}))


class ChangeUserForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=32,error_messages={'required': '不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','value':"1",'name':'username'}))
    email = forms.CharField(label='邮 箱',min_length=6,max_length=64,
                                error_messages={'required': '邮箱不能为空', 'min_length': '密长度不能小于6',
                                                'max_length': '长度不能大于64', },
                                widget=forms.EmailInput(
                                    attrs={'class': 'form-control', 'name':'email','value':'{{ user_obj.email }}'}))

class AddNavigationForm(forms.Form):
    website_name = forms.CharField(label='网站名',max_length=32,error_messages={'required': '不能为空'},
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','name':'website_name'}))
    website_url = forms.CharField(label='网站名', max_length=32, error_messages={'required': '不能为空'},
                                  validators=[],
                                   widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '', 'name': 'website_url'}))



class CreateServerForm(forms.Form):
    server_name = forms.CharField(label='服务器名',min_length=1,max_length=32,error_messages={'required': '不能为空'},
                                  validators=[user_auth],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','name':'server_name'}))
    ip = forms.CharField(label='ip',min_length=7,max_length=16,error_messages={'required': '不能为空'},
                         validators=[is_ip,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','name':'ip'}))
    user = forms.CharField(label='ssh账号',required=False,min_length=0,max_length=16,error_messages={},
                           validators=[user_auth,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','name':'ssh_user'}))
    password = forms.CharField(label='ssh密码',required=False,min_length=0,max_length=32,error_messages={},
                               validators=[password_auth,],
                               widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'','name':'ssh_password'}))
    ssh_port = forms.IntegerField(label='ssh端口',required=False,error_messages={},
                                  validators=[is_digital,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','name':'ssh_port'}))


class CreateServerGroupForm(forms.Form):
    group = forms.CharField(label='服务器组',max_length=32,error_messages={'required': '不能为空'},validators=[password_auth,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','required':'','name':'group'}))



class CreateProjectForm(forms.Form):
    title = forms.CharField(label='项目名',max_length=64,error_messages={'required': '不能为空'},validators=[special_auth,],
                                widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': '', 'name': 'title'}))
    describe = forms.CharField(label='项目名', max_length=512, required=False,
                            widget=forms.Textarea(
                                attrs={'class': 'form-control', 'name': 'describe','rows':'3'}))

    git_url = forms.CharField(label='git url', max_length=128,
                               widget=forms.URLInput(
                                   attrs={'class': 'form-control','name':'git_url'}))
    git_user = forms.CharField(label='git url', max_length=16,required=False,
                              validators=[user_auth, ],
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'name': 'git_user'}))
    git_passowrd = forms.CharField(label='git密码', max_length=64, required=False,
                               validators=[password_auth, ],
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'name': 'git_passowrd'}))
    git_ssh_key = forms.CharField(label='git ssh-key', max_length=2048, required=False,
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control', 'rows':'3','name': 'git_ssh_key'}))
    git_branch = forms.CharField(label='git branch', max_length=16,
                               validators=[special_auth,],
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'name': 'git_branch'}))
    deploy_dir = forms.CharField(label='项目路径', max_length=512,
                                 validators=[special_auth, ],
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'name': 'deploy_dir'}))

    exclude_file = forms.CharField(label='项目名', max_length=4096, required=False,
                            widget=forms.Textarea(
                                attrs={'class': 'form-control', 'name': 'exclude_file','rows':'3'}))
    dingding_notice = forms.CharField(label='git branch', max_length=128, required=False,
                               widget=forms.URLInput(
                                   attrs={'class': 'form-control', 'name': 'dingding_notice'}))

class CreateServerUserForm(forms.Form):
    username = forms.CharField(label='姓名',max_length=32,error_messages={'required': '不能为空'},
                                validators=[user_auth,],
                               widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'','name':'username'}))
    password = forms.CharField(label='密 码', min_length=6, max_length=64,
                               error_messages={'required': '密码不能为空',},
                               validators=[password_auth,],
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control','required': '','name':'password'
                                          }))
    uid = forms.IntegerField(label='UID',required=False,
                          validators=[ugid_auth,],
                             widget=forms.TextInput(attrs={'class': 'form-control','name':'uid'}))
    gid = forms.IntegerField(label='GID',required=False,
                          validators=[ugid_auth,],
                          widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'name': 'gid'}))
    sudo = forms.CharField(label='sudo',max_length=1024,required=False,
                            validators=[sudo_auth,],
                           widget=forms.Textarea(attrs={'class':'form-control','rows':'3','placeholder':''})
                           )
class EditServerUserForm(forms.Form):
    password = forms.CharField(label='密 码', min_length=6, max_length=64,
                               error_messages={'required': '密码不能为空',},
                               validators=[password_auth,],
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control','required': '','name':'password'
                                          }))
    sudo = forms.CharField(label='sudo', max_length=1024, required=False,
                           validators=[sudo_auth, ],
                           widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': ''})
                           )


