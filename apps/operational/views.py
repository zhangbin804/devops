from django.shortcuts import render, HttpResponse, redirect
from apps.operational.create import password
from django.db.models import Q
import re
from apps.operational.core.server_group import *
from apps.accounts.forms.forms import CreateServerForm,CreateServerGroupForm,CreateServerUserForm,EditServerUserForm
from apps.accounts.core.accounts_auth import auth,get_user_id
from apps.operational.models import *
from lib.page import PagerObj
from django.utils.safestring import mark_safe


@auth
def CreatePassword(request):
    if request.method == 'GET':
        return render(request,'operational/password.html')

    if request.method == 'POST':
        password_type = request.POST.get('password_type')
        length = int(request.POST.get('length',16))
        passwd = password.random_str(password_type,length)
        return render(request,'operational/password.html',{'passwd':passwd})

@auth
def CreateServer(request):
    if request.method == 'GET':
        form = CreateServerForm()
        server_group_list = Group.objects.all()
        return render(request,'operational/create_server.html',{'form':form,'server_group_list':server_group_list})
    if request.method == 'POST':
        server_group_list = Group.objects.all()
        form = CreateServerForm(request.POST)
        try:
            option_server = get_option_server(request)
        except Exception as e:
            error_msg = '未选择组'
            return render(request, 'operational/create_server.html',
                          {'form': form, 'server_group_list': server_group_list, 'error_msg': error_msg})
        if form.is_valid():
            create_server_dict = create_edit_server_dict(request)
            try:
                create_server = Server.objects.create(**create_server_dict)
            except Exception as e:
                error_msg = '添加失败'
                return render(request, 'operational/create_server.html',
                              {'form': form, 'server_group_list': server_group_list,'error_msg':error_msg})
            server_id = create_server.id
            for i in option_server:
                add_group = Server.objects.filter(id=server_id).first().groups.add(i)
            return redirect('/operational/list/server/')
        else:
            return render(request, 'operational/create_server.html', {'form': form,'server_group_list':server_group_list})



@auth
def ServerList(request):
    if request.method == 'GET':
        current_page = int(request.GET.get('p', 1))
        search = request.GET.get('search', '')
        total_num = int(request.session["total_num"])
        server_all = Server.objects.all()
        if search:
            server_all = server_all.filter(Q(server_name__contains=search)|Q(ip__contains=search))
        page = PagerObj(current_page, '/operational/list/server/?search={}'.format(search), server_all, total_num)
        pager, server_list = page.pages()
        return render(request,'operational/server_list.html',{'server_list':server_list,'pager': mark_safe(pager)})

@auth
def GetEditServer(request):
    if request.method == 'GET':
        server_id = request.path.split('/')[-2]
        get_edit_server = edit_read_server(server_id)
        return render(request,'operational/edit_server.html',get_edit_server)
    return HttpResponse('edit server')

@auth
def PostEditServer(request):
    if request.method == 'POST':
        option_server = get_option_server(request)
        server_id = request.POST.get('server_id')
        referer = re.findall(r'/operational/edit/server/.*',str(request.META['HTTP_REFERER']))[0]
        form = CreateServerForm(request.POST)
        if form.is_valid():
            change_server_dict = create_edit_server_dict(request)
            try:
                change_server = Server.objects.filter(id=server_id).update(**change_server_dict)
            except Exception as e:
                print(e)
                return redirect(referer)
            group_obj = Server.objects.filter(id=server_id).first()
            group_obj.groups.clear()
            for i in option_server:
                group_obj.groups.add(i)
            return redirect('/operational/list/server/')
        return redirect(referer)


@auth
def DeleteServer(request):
    if request.method == 'POST':
        server_id = request.POST.get('server_id')
        server_obj = Server.objects.filter(id=server_id)
        delete_server_group = server_obj.first().groups.clear()
        delete_server = Server.objects.filter(id=server_id).delete()
        return HttpResponse('success')

@auth
def ReadServer(request):
    if request.method == 'GET':
        server_id = request.path.split('/')[-2]
        read_server = edit_read_server(server_id)
        return render(request,'operational/read_server.html',read_server)

@auth
def CreateGroup(request):
    if request.method == 'GET':
        form = CreateServerGroupForm()
        return render(request,'operational/create_server_group.html',{'form':form})
    if request.method == 'POST':
        form = CreateServerGroupForm(request.POST)
        if form.is_valid():
            group = request.POST.get('group')
            add_group = Group.objects.create(title=group)
            return redirect('/operational/list/group/')
        return render(request, 'operational/create_server_group.html', {'form': form})

@auth
def DeleteGroup(request):
    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        group_obj = Group.objects.get(id=group_id)
        group_obj.server_set.clear()
        delete_group = Group.objects.filter(id=group_id).delete()
        return HttpResponse('delete group')

@auth
def GroupList(request):
    if request.method == 'GET':
        current_page = int(request.GET.get('p', 1))
        search = request.GET.get('search', '')
        total_num = int(request.session["total_num"])
        group_all = Group.objects.all()
        server_group_dict = get_group_server(group_all)
        if search:
            group_all = group_all.filter(title__contains=search)
        page = PagerObj(current_page, '/operational/list/group/?search={}'.format(search), group_all, total_num)
        pager, group_list = page.pages()
        return render(request,'operational/group_list.html',
                      {'group_list':group_list,'pager': mark_safe(pager),'server_group_dict':server_group_dict})

@auth
def GetEditGroup(request):
    if request.method == 'GET':
        group_id = request.path.split('/')[-2]
        get_edit_group = edit_read_group(group_id)
        return render(request,'operational/edit_group.html',get_edit_group)

@auth
def PostEditGroup(request):
    if request.method == 'POST':
        option_server = get_option_server(request)
        form = CreateServerGroupForm(request.POST)
        group_title = request.POST.get('group')
        group_id = request.POST.get('group_id')
        if form.is_valid():
            change_group_server_obj = Group.objects.get(id=group_id)
            old_host = get_group_ip_str(change_group_server_obj.server_set.all())
            ssh_user_list = get_remove_ssh_user_list(change_group_server_obj.serveruser_set.all())
            if old_host and ssh_user_list:
                for i in ssh_user_list:
                    remove_user_or_sudo(i)
            change_group_server_obj.server_set.clear()
            for i in option_server:
                change_group_server_obj.server_set.add(i)
            new_host = get_group_ip_str(change_group_server_obj.server_set.all())
            if new_host and ssh_user_list:
                for i in ssh_user_list:
                    create_server_ssh_user(i)
                    if ServerUser.objects.get(id=i).sudo:
                        create_server_ssh_user_sudo(i)
            if change_group_server_obj.title != group_title:
                change_group_title = Group.objects.filter(id=group_id).update(title=group_title)
            return redirect('/operational/list/group/')
        return redirect(request.path+str(group_id)+'/')

@auth
def ReadGroup(request):
    if request.method == 'GET':
        group_id = request.path.split('/')[-2]
        get_edit_group = edit_read_group(group_id)
        return render(request, 'operational/read_group.html', get_edit_group)


@auth
def ListServerUser(request):
    if request.method == 'GET':
        current_page = int(request.GET.get('p', 1))
        search = request.GET.get('search', '')
        total_num = int(request.session["total_num"])
        server_user_all = ServerUser.objects.all()
        if search:
            server_user_all = server_user_all.filter(Q(username__contains=search)|Q(groups__title__contains=search)|Q(servers__server_name__contains=search))
        page = PagerObj(current_page, '/operational/server/list/user/?search={}'.format(search), server_user_all, total_num)
        pager, server_user_list = page.pages()
        return render(request,'operational/list_server_user.html',{'server_user_list':server_user_list,'pager': mark_safe(pager)})

@auth
def CreateServerUser(request):
    if request.method == 'GET':
        form = CreateServerUserForm()
        all_server_list = Server.objects.all()
        all_group_list = Group.objects.all()
        return render(request,'operational/create_server_user.html',
                      {'form':form,'all_server_list':all_server_list,'all_group_list':all_group_list})
    if request.method == 'POST':
        form = CreateServerUserForm(request.POST)
        all_group_list = Group.objects.all()
        all_server_list = Server.objects.all()
        if form.is_valid():
            try:
                create_server_user = create_edit_server_user(request)
            except Exception as e:
                error_msg = '添加失败'
                return render(request, 'operational/create_server_user.html',
                              {'form': form, 'all_server_list': all_server_list, 'all_group_list': all_group_list,'error_msg':error_msg})
            create_server_ssh_user(create_server_user.id)
            create_server_ssh_user_sudo(create_server_user.id)
            return redirect('/operational/server/list/user/')
        return render(request, 'operational/create_server_user.html',
                      {'form': form, 'all_server_list': all_server_list, 'all_group_list': all_group_list})

@auth
def EditServerUser(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        server_user_obj = ServerUser.objects.get(id=id)
        id_list = get_server_or_group_id(server_user_obj)
        all_server_list = Server.objects.all()
        all_group_list = Group.objects.all()
        return render(request,'operational/edit_server_user.html',
                     {'server_user_obj':server_user_obj,'all_server_list':all_server_list,'all_group_list':all_group_list,'id_list':id_list})
    if request.method == 'POST':
        form = EditServerUserForm(request.POST)
        id = request.POST.get('id')
        if form.is_valid():
            edit_server_user = create_edit_server_user(request,use='edit')
            create_server_ssh_user(id)
            if ServerUser.objects.get(id=id).sudo:
                create_server_ssh_user_sudo(id)
            return redirect('/operational/server/list/user/')
        return redirect('/operational/server/edit/user/?id=%s'%(request.POST.get('id')))


@auth
def DeleteServerUser(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        remove_user_or_sudo(user_id)
        delete_server_user = ServerUser.objects.filter(id=user_id).delete()
        return HttpResponse('delete')

@auth
def ReadServerUser(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        server_user_obj = ServerUser.objects.get(id=id)
        id_list = get_server_or_group_id(server_user_obj)
        all_server_list = Server.objects.all()
        all_group_list = Group.objects.all()
        return render(request,'operational/read_server_user.html',
                     {'server_user_obj':server_user_obj,'all_server_list':all_server_list,'all_group_list':all_group_list,'id_list':id_list})
