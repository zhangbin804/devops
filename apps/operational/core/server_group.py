from apps.operational.models import *
import time
from lib.Ansiable.ansible_server_user import *


def get_host(server_user_id):
    host_srt = ''
    server_user_obj = ServerUser.objects.get(id=server_user_id)
    
    if server_user_obj.way == 1:
        for i in server_user_obj.servers.all():
            if host_srt:
                host_srt = host_srt + ','+i.ip
            else:
                host_srt = i.ip
    elif server_user_obj.way == 2:
        for i in server_user_obj.groups.all():
            for j in i.server_set.all():
                if host_srt:
                    host_srt = host_srt + ',' + j.ip
                else:
                    host_srt = j.ip
    return host_srt


def get_user(id):
    server_user_obj = ServerUser.objects.get(id=id)
    user = server_user_obj.username
    return user

def get_server_user_ansible(id):
    ansible_user_dict = {}
    server_user_obj = ServerUser.objects.get(id=id)
    ansible_user_dict['host'] = get_host(id)
    ansible_user_dict['user'] = server_user_obj.username
    ansible_user_dict['password'] = server_user_obj.password
    ansible_user_dict['uid'] = server_user_obj.uid
    ansible_user_dict['gid'] = server_user_obj.gid
    ansible_user_dict['sudo'] = server_user_obj.sudo
    return ansible_user_dict


def create_server_ssh_user(id):
    server_user_obj = ServerUser.objects.get(id=id)
    host = get_host(id)
    user = server_user_obj.username
    uid = None
    gid = None
    password = encryption_password(server_user_obj.password)
    if server_user_obj.uid:
        uid = server_user_obj.uid
    if server_user_obj.gid:
        gid = server_user_obj.gid
    create_user_log = create_server_user(host=host,user=user,password=password,uid=uid,gid=gid)
    return create_user_log

def create_server_ssh_user_sudo(id):
    server_user_obj = ServerUser.objects.get(id=id)
    host = get_host(id)
    user = server_user_obj.username
    sudo = server_user_obj.sudo
    if server_user_obj.sudo:
        user_sudo(host=host,user=user,sudo=sudo)


def remove_user_or_sudo(id):
    server_user_obj = ServerUser.objects.get(id=id)
    host = get_host(id)
    user = server_user_obj.username
    remove_server_user(host=host,user=user)
    remove_user_sudo(host=host,user=user)
    return 1


def create_time():
    import time
    ctime = time.strftime('%Y-%m-%d %X')
    return ctime

def get_group_server(group_all):
    server_group_dict = {}
    for group in group_all:
        user_list = Group.objects.get(id=group.id).server_set.all()
        group_user = ''
        for server in user_list:
            if group_user:
                group_user = group_user + '|' + server.server_name
            else:
                group_user = server.server_name
        server_group_dict[group.id] = group_user
    return server_group_dict


def get_server_group_list(server_id):
    server_group = Server.objects.filter(id=server_id).first().groups.all()
    server_group_id_list = []
    for i in server_group:
        server_group_id_list.append(i.id)
    return server_group,server_group_id_list

def edit_read_server(server_id):
    server_group_list = Group.objects.all()
    server_obj = Server.objects.filter(id=server_id).all()
    for i in server_obj: server_obj = i
    group, group_id = get_server_group_list(server_id)
    get_server_group_list(server_id)
    return {'server_obj':server_obj,'group':group,'server_group_list':server_group_list,'group_id':group_id}

def get_group_server_list(group_id):
    group_server = Group.objects.get(id=group_id).server_set.all()
    group_server_id_list = []
    for i in group_server:
        group_server_id_list.append(i.id)
    return group_server,group_server_id_list

def edit_read_group(group_id):
    group_obj = Group.objects.filter(id=group_id).all()
    for i in group_obj: group_obj = i
    all_server = Server.objects.all()
    group_server, group_server_id_list = get_group_server_list(group_id)
    return {'group_obj':group_obj,'group_server':group_server,'all_server':all_server,'group_server_id_list':group_server_id_list}


def get_option_server(request):
    option_server = ''
    for i in request.POST.lists():
        if i[0] == 'option_server' and bool(i[0]):
            option_server = i[1]
    return option_server

def get_group_ip_str(group_obj):
    host = ''
    for i in group_obj:
        if host:
            host = host + i.ip
        else:
            host = i.ip
    return host

def get_remove_ssh_user_list(group_obj):
    id_list = []
    for i in group_obj:
        id_list.append(i.id)
    return id_list




def create_edit_server_dict(request):
    request_server_dict = {}
    request_server_dict['server_name'] = request.POST.get('server_name')
    request_server_dict['ip'] = request.POST.get('ip')
    if request.POST.get('user'):
        request_server_dict['user'] = request.POST.get('user')
    if request.POST.get('password') != '******':
        request_server_dict['password'] = request.POST.get('password')
    if request.POST.get('ssh_port'):
        request_server_dict['port'] = int(request.POST.get('ssh_port'))
    return request_server_dict



def create_edit_server_user(request,use='create'):
    server_user_dict = {}
    if use == 'create':
        server_user_dict['username'] = request.POST.get('username')
        server_user_dict['password'] = request.POST.get('password')
        if request.POST.get('senior',0):
            server_user_dict['senior'] = 1
        if request.POST.get('way'):
            server_user_dict['way'] = int(request.POST.get('way'))
            if request.POST.get('uid'):
                server_user_dict['uid'] = int(request.POST.get('uid'))
            if request.POST.get('gid'):
                server_user_dict['gid'] = int(request.POST.get('gid'))
            if request.POST.get('sudo'):
                server_user_dict['sudo'] = request.POST.get('sudo')
            server_user_dict['create_time'] = create_time()
            create_server_user = ServerUser.objects.create(**server_user_dict)
            if server_user_dict['way'] == 1:
                option_server = None
                for i in request.POST.lists():
                    if i[0] == 'option_server':
                        option_server = i[1]
                if option_server:
                    create_server_user.servers.add(*option_server)
            elif server_user_dict['way'] == 2:
                if request.POST.get('group'):
                    create_server_user.groups.add(request.POST.get('group'))
        else:
            create_server_user = ServerUser.objects.create(**server_user_dict)
        return create_server_user
    elif use == 'edit':
        id = request.POST.get('id')
        host = get_host(id)
        user = get_user(id)
        if request.POST.get('password') != '******':
            server_user_dict['password'] = request.POST.get('password')
        if request.POST.get('senior',0):
            server_user_dict['senior'] = 1

        server_user_dict['sudo'] = request.POST.get('sudo')
        server_user_obj = ServerUser.objects.get(id=id)
        if int(request.POST.get('way')) == server_user_obj.way:
            if server_user_obj.way == 1:
                remove_server_user(host,user)
                remove_user_sudo(host,user)
                server_user_obj.servers.clear()
                option_server = None
                for i in request.POST.lists():
                    if i[0] == 'option_server':
                        option_server = i[1]
                if option_server:
                    server_user_obj.servers.add(*option_server)
            elif server_user_obj.way == 2:
                remove_server_user(host,user)
                remove_user_sudo(host,user)
                server_user_obj.groups.clear()
                if request.POST.get('group'):
                    server_user_obj.groups.add(request.POST.get('group'))
        elif int(request.POST.get('way')) == 0:
            if server_user_obj.way == 1:
                remove_server_user(host, user)
                remove_user_sudo(host, user)
                server_user_obj.servers.clear()
            elif server_user_obj.way == 2:
                remove_server_user(host, user)
                remove_user_sudo(host, user)
                server_user_obj.groups.clear()
        elif int(request.POST.get('way')) == 1:
            if  server_user_obj.way == 2:
                remove_server_user(host, user)
                remove_user_sudo(host, user)
                server_user_obj.groups.clear()
                option_server = None
                for i in request.POST.lists():
                    if i[0] == 'option_server':
                        option_server = i[1]
                if option_server:
                    server_user_obj.servers.add(*option_server)
        elif int(request.POST.get('way')) == 2:
            if server_user_obj.way == 1:
                remove_server_user(host, user)
                remove_user_sudo(host, user)
                server_user_obj.servers.clear()
                if request.POST.get('group'):
                    server_user_obj.groups.add(request.POST.get('group'))
        server_user_dict['way'] = int(request.POST.get('way'))
        update_server_user = ServerUser.objects.filter(id=id).update(**server_user_dict)
        return update_server_user


def get_server_or_group_id(server_user_obj):
    id_list = []
    if server_user_obj.way == 1:
        for i in server_user_obj.servers.all():
            id_list.append(i.id)
        return id_list
    elif server_user_obj.way == 2:
        for i in server_user_obj.groups.all():
            id_list = i.id
        return id_list


