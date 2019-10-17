from django.shortcuts import render, HttpResponse, redirect
from apps.permissions import models as permissions_models
from apps.accounts.core.accounts_auth import auth,get_user_id
from django.db.models import Count
from django.utils.safestring import mark_safe
from lib.page import PagerObj
from django.db.models import Q
import time
from apps.permissions.core.permissions_views import create_edit_user
from apps.accounts.forms.forms import CreateUserForm,CreateRolesForm,ChangeUserForm

@auth
def ListPermissions(request):
    if request.method == 'GET':
        permission_dict = {}
        roles_id_list = permissions_models.Role.objects.all()
        for id in roles_id_list:
            user_list = permissions_models.Role.objects.get(id=id.id).user_set.all()
            roles_user = ''
            for user in user_list:
                if roles_user:
                    roles_user = roles_user + ' ' + str(user.name)
                else:
                    roles_user = str(user.username)
            permission_dict[id.title] = roles_user
        return render(request,'permissions/list.html',{'permission_dict':permission_dict})

@auth
def EditPermissions(request):
    if request.method == 'GET':
        user = request.session['user']
        role_id = int(request.path.split('/')[-2])
        roles_title = permissions_models.Role.objects.get(id=role_id).title
        all_permission_dict = {}
        all_permission = permissions_models.Permission.objects.all()
        for index in range(len(all_permission.values("id"))):
            try:
                if all_permission_dict[all_permission.values("codes")[index]["codes"]]:
                    all_permission_dict[all_permission.values("codes")[index]["codes"]][
                        all_permission.values("id")[index]['id']] = all_permission.values("title")[index]['title']
                else:
                    all_permission_dict[all_permission.values("codes")[index]["codes"]] = {}
            except Exception as e:
                all_permission_dict[all_permission.values("codes")[index]["codes"]] = {}
            all_permission_dict[all_permission.values("codes")[index]["codes"]][
                all_permission.values("id")[index]['id']] = all_permission.values("title")[index]['title']
        all_codes = permissions_models.Permission.objects.values('codes').annotate(authorNum=Count("codes"))
        old_roles_permission = permissions_models.Role.objects.all().filter(id=role_id).values("permissions__id")
        old_roles_permission_id_list = []
        for i in old_roles_permission:
            old_roles_permission_id_list.append(i['permissions__id'])

        return render(request, 'permissions/editPermissions.html', {'all_permission_dict':all_permission_dict, 'roles_id':role_id, 'old_roles_permission_id_list':old_roles_permission_id_list})

@auth
def ChangePermissions(request):
    if request.method == 'POST':
        roles_id = request.POST.get('roles')
        if not roles_id:
            return HttpResponse('error: not roles ')
        permission = request.POST.lists()
        permission_all_list = []
        permission_id_list = []
        for i in permission:
            permission_all_list.append(i[1])
        for i in permission_all_list[1]:
            if i:
                permission_id_list.append(i)
        change_role_table = permissions_models.Role.objects.filter(id=roles_id).first()
        change_role_table.permissions.clear()
        change_role_table.permissions.add(*permission_id_list)
        return redirect('/permissions/list/')

@auth
def ListUser(request):
    if request.method == 'GET':
        current_page = int(request.GET.get('p',1))
        search = request.GET.get('search','')
        total_num = 10
        user_obj = permissions_models.User.objects.all()
        if search:
            user_obj = user_obj.filter(Q(name__contains=search)|Q(username__contains=search)|Q(email__contains=search))
        page = PagerObj(current_page, '/permissions/list/user/?search={}'.format(search), user_obj, total_num)
        pager, user_list = page.pages()
        return render(request,'permissions/user_list.html',{'user_list':user_list,'pager': mark_safe(pager)})

@auth
def EditUser(request):
    if request.method == 'GET':
        user_id = request.path.split('/')[-2]
        user_obj = permissions_models.User.objects.get(id=user_id)
        # for i in user_obj:user_obj = i
        role_list = permissions_models.Role.objects.all()
        role = permissions_models.User.objects.get(id=int(user_id)).roles.values('user__roles')[0]['user__roles']
        return render(request,'permissions/edit_user.html',{'user_obj':user_obj,'role_list':role_list,'role':role})

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_dict = create_edit_user(request,use='edit')
        role = request.POST.get('role')
        update_user = permissions_models.User.objects.filter(id=int(user_id)).update(**user_dict)
        update_role = permissions_models.User.objects.filter(id=int(user_id)).first().roles.set(str(role))
        return redirect('/permissions/list/user/')

@auth
def DisableUser(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        old_disable = permissions_models.User.objects.filter(id=id).values('disable')[0]['disable']
        new_disable = 0
        if old_disable == 0:
            new_disable = 1
        elif old_disable == 1:
            new_disable == 0
        update_disable = permissions_models.User.objects.filter(id=id).update(disable=new_disable)
        return  HttpResponse('ok')


@auth
def DeleteUser(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id','')
        if user_id:
            delete_user = permissions_models.User.objects.filter(id=user_id).delete()
            return HttpResponse('success')
        return HttpResponse('error')

@auth
def CreateUser(request):
    if request.method == 'GET':
        form = CreateUserForm()
        role_list = permissions_models.Role.objects.all()
        return render(request,'permissions/create_user.html',{'form':form,'role_list':role_list})
    if request.method == 'POST':
        form = CreateUserForm()
        role_list = permissions_models.Role.objects.all()
        user_dict = create_edit_user(request)
        user_dict['name'] =  request.POST.get('user')
        user_check = permissions_models.User.objects.filter(name=user_dict['name'])
        if not user_check.first():
            role = request.POST.get('role',2)
            create_user = permissions_models.User.objects.create(**user_dict)
            if create_user:
                add_role = permissions_models.User.objects.filter(name=user_dict['name'],username=user_dict['username']).first().roles.add(role)
                return redirect('/permissions/list/user/')
            error_msg = '添加失败!'
            return render(request, 'permissions/create_user.html', {'form': form, 'role_list': role_list,'error_msg':error_msg})
        error_msg = '账号已存在!'
        return render(request, 'permissions/create_user.html', {'form': form, 'role_list': role_list,'error_msg':error_msg})


@auth
def CreateRoles(request):
    if request.method == 'GET':
        form = CreateRolesForm()
        return render(request,'permissions/create_roles.html',{'form':form})
    if request.method == 'POST':
        form = CreateRolesForm(request.POST)
        if form.is_valid():
            role = form.clean()["role"]
            check_role = permissions_models.Role.objects.filter(title=role).first()
            if not check_role:
                create_role = permissions_models.Role.objects.create(title=role)
                return redirect('/permissions/list/')
            error_msg = '角色组已存在！'
            form = CreateRolesForm()
            return render(request, 'permissions/create_roles.html', {'form': form,'error_msg':error_msg})

@auth
def DeleteRoles(request):
    if request.method == 'POST':
        role = request.POST.get('role_id')
        protection_role_list = [1,2]
        defautl_id = 2
        roles_user_list = permissions_models.Role.objects.get(id=role).user_set.all()
        if role in protection_role_list:
            return HttpResponse('delete failed')
        try:
            if roles_user_list.first():
                for user in roles_user_list:
                    update_user_roles = permissions_models.User.objects.filter(name=str(user)).first().roles.set(str(defautl_id))
            delete_role = permissions_models.Role.objects.filter(id=role).delete()
        except Exception as e:
            return HttpResponse('error')
        return HttpResponse('success')

