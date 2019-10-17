from django.shortcuts import render,HttpResponse,redirect
from apps.operational.models import Group
from apps.accounts.core.accounts_auth import auth
from apps.permissions.models import Role
from apps.accounts.forms.forms import CreateProjectForm
from apps.project.core.project_views import *
from django.db.models import Q
from lib.page import PagerObj
from django.utils.safestring import mark_safe

@auth
def ListProject(request):
    if request.method == 'GET':
        current_page = int(request.GET.get('p', 1))
        search = request.GET.get('search', '')
        total_num = int(request.session["total_num"])
        project_all = Project.objects.all()
        if search:
            project_all = project_all.filter(Q(title__contains=search) | Q(describe__contains=search) | Q(server_group__title__contains=search))
        page = PagerObj(current_page, '/project/list/?search={}'.format(search), project_all, total_num)
        pager, project_list = page.pages()
        return render(request,'project/project_list.html',{'project_list':project_list,'pager': mark_safe(pager)})

@auth
def CreateProject(request):
    if request.method == 'GET':
        server_group_all = Group.objects.all()
        role_all = Role.objects.all()
        form = CreateProjectForm()
        return render(request,'project/create_project.html',{'server_group_all':server_group_all,'form':form,'role_all':role_all})
    if request.method == 'POST':
        form = CreateProjectForm(request.POST)
        server_group_all = Group.objects.all()
        role_all = Role.objects.all()
        if form.is_valid():
            project_dict = create_project_dict(request)
            create_project = Project.objects.create(**project_dict)
            if not create_project:
                error_msg = '添加失败'
                return render(request,'project/create_project.html',{'server_group_all':server_group_all,'form':form,'role_all':role_all,'error_msg':error_msg})
            return redirect('/project/list/')
        return render(request,'project/create_project.html',{'server_group_all':server_group_all,'form':form,'role_all':role_all})

@auth
def EditProject(request):
    if request.method == 'GET':
        project_id = request.GET.get('id')
        project_obj = Project.objects.get(id=project_id)
        server_group_all = Group.objects.all()
        role_all = Role.objects.all()
        return render(request,'project/edit_project.html',{'project_obj':project_obj,'server_group_all':server_group_all,'role_all':role_all})
    if request.method == 'POST':
        server_group_all = Group.objects.all()
        role_all = Role.objects.all()
        form = CreateProjectForm(request.POST)
        project_id = request.POST.get('project_id')
        if form.is_valid():
            project_dict = create_project_dict(request)
            change_project = Project.objects.filter(id=project_id).update(**project_dict)
            if not change_project:
                error_msg = '修改失败'
                return render(request,'project/create_project.html',{'server_group_all':server_group_all,'form':form,'role_all':role_all,'error_msg':error_msg})
            return redirect('/project/list/')
        return render(request, 'project/create_project.html',
                      {'server_group_all': server_group_all, 'form': form, 'role_all': role_all})

@auth
def DeleteProjetc(request):
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        delete_project = Project.objects.filter(id=project_id).delete()
        return HttpResponse('delete project')

@auth
def ReadProject(request):
    if request.method == 'GET':
        project_id = request.GET.get('id')
        project_obj = Project.objects.get(id=project_id)
        server_group_all = Group.objects.all()
        role_all = Role.objects.all()
        return render(request,'project/read_project.html',{'project_obj':project_obj,'server_group_all':server_group_all,'role_all':role_all})

@auth
def GetTag(request):
    if request.method == 'POST':
        id = request.POST.get('update_project_id')
        project_obj = Project.objects.get(id=id)
        if project_obj.work_dir:
            home_dir = os.getcwd()
            git = GitApi()
            git.git_dir(project_obj.work_dir)
            tag_all = git.linux_get_origin_tag()
            tag_list_str = ''
            tag_list = tag_all.split('\n')
            for i in tag_list:
                if i:
                    if tag_list_str:
                        tag_list_str = tag_list_str + ',' + i
                    else:
                        tag_list_str = i
            os.chdir(home_dir)
            return HttpResponse(tag_list_str)
        else:
            return HttpResponse(1)

@auth
def ConnectionTestAuth(request):
    if request.method == 'GET':
        import shutil,os
        WORK_HOME = 'work/project/'
        id = request.GET.get('id')
        project_obj = Project.objects.get(id=id)
        status_code = 0
        git_work_dir = ''
        if project_obj.connection_auth  and project_obj.work_dir:
            git_work_dir = project_obj.work_dir
            if os.path.isdir(git_work_dir):
                shutil.rmtree(git_work_dir)

        project_dir_name = random_str(types='type5',randomlength=10)
        git_work_dir = WORK_HOME + project_dir_name
        print('git_work_dir ',git_work_dir )
        home_dir = os.getcwd()
        git_url = auth_git_url(id)
        git = GitApi()
        git.clone(clone_url=git_url,branch=project_obj.git_branch,path=git_work_dir)
        try:
            git.git_dir(git_work_dir)
        except Exception as e:
            project_obj.connection_auth = 1
            project_obj.save()
            return redirect('/project/list/')
        os.chdir(home_dir)
        project_obj.connection_auth = 2
        project_obj.work_dir = git_work_dir
        project_obj.save()
        return redirect('/project/list/')

@auth
def UpdateProject(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST.get('id')
        tag = ''
        if request.POST.get('update_project_way') and request.POST.get('tag'):
            tag = request.POST.get('tag')
        update_project = update_project_views(id, tag=tag)
        if not update_project:
            return HttpResponse('src目录错误')
        print(request.POST)
        project_log_id,log_dict = get_git_information_log(id,request,update_project)
        print('iiiiiiiiiiiiiiiiiiiiiiiddddddddddddddddd',project_log_id)
        update_project_log = Project.objects.filter(id=id).update(log=project_log_id)
        project_obj = Project.objects.get(id=id)
        send_project(project_obj)
        return redirect('/project/list/')
        

@auth
def RollbackProject(request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST.get('id')
        project_obj = Project.objects.get(id=id)
        rollback_project_dict = clone_project_dict(id)
        way = request.POST.get('rollbac_project_way')
        commit_id = ''
        if way == '0':
            commit_id = Log.objects.get(id=project_obj.log.on_version_log_id).git_commit
            rollback_project_dict['git_tag']  = Log.objects.get(id=project_obj.log.on_version_log_id).git_tag
        elif way == '2':
            commit_id = request.POST.get('rollback_project_commit_input')

        if not commit_id:
            return HttpResponse('未指定commit 版本')
        rollback_project_dict['git_commit'] = commit_id
        run_rollback = rollback_ansible_run(rollback_project_dict)
        if not run_rollback:
            return HttpResponse('src目录错误')
        project_log_id,log_dict = get_git_information_log(id,request,run_rollback)
        update_project_log = Project.objects.filter(id=id).update(log=project_log_id)
        project_obj = Project.objects.get(id=id)
        send_project(project_obj,use='rollback')
        return redirect('/project/list/')

