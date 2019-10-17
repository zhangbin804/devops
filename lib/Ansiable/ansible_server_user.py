import os
from time import time
from lib.Ansiable.yaml.server_user_yaml import *
import crypt
from lib.Ansiable.ansible_runner import *



def encryption_password(password):
    key = 'devops'
    encryption_str = crypt.crypt(password,key)
    return encryption_str



def ansible_run(yaml_model):
    filename = 'lib/Ansiable/yaml/' + str(time()).replace('.', '') + '.yaml'
    with open(filename,'w',encoding='utf8') as f:
        f.write(yaml_model)
    print(yaml_model)
    ansible = ansible_Runner('/etc/ansible/hosts')
    ansible.run_playbook(filename)
    print(ansible.get_result())
    os.remove(filename)
    return ansible.get_result()


def create_server_user(host,user,password,uid=None,gid=None):
    yaml_model = None
    if uid and gid:
        yaml_model = ADD_SUERVER_USER_UGID_YAML.format(host=host,user=user,password=password,uid=uid,gid=gid)
    elif uid:
        yaml_model = ADD_SUERVER_USER_UID_YAML.format(host=host,user=user,password=password,uid=uid)
    elif gid:
        yaml_model = ADD_SUERVER_USER_GID_YAML.format(host=host,user=user,password=password,gid=gid)
    else:
        yaml_model = ADD_SUERVER_USER_YAML.format(host=host,user=user,password=password)
    ansible_run(yaml_model)

def remove_server_user(host,user):
    yaml_model = REMOVE_SERVER_USER_YAML.format(host=host,user=user)
    ansible_run(yaml_model)

def user_sudo(host,user,sudo):
    yaml_model = SUDO_YAML.format(host=host,user=user,sudo=sudo)
    ansible_run(yaml_model)

def remove_user_sudo(host,user):
    yaml_model = REMOVE_SUDO_YAML.format(host=host,user=user)
    ansible_run(yaml_model)


