from django.shortcuts import render, HttpResponse, redirect
from apps.accounts.forms import forms
from apps.accounts.core.accounts_auth import auth,get_user_id
from django.conf import settings
from lib.email import Mail,ProcessMail
import time
import json
from django.db.models import Q
from apps.process import models as process_models
from apps.permissions.models import User
from lib.page import PagerObj
from django.utils.safestring import mark_safe
from apps.process.core.option_process import *



@auth
def ListProcess(request):
    if request.method == 'GET':
        current_page = request.GET.get('p',1)
        search = request.GET.get('search','')
        total_num = int(request.session["total_num"])
        current_page = int(current_page)
        process_all = process_models.Process.objects.all()
        if search:
            process_all = process_all.filter(Q(name__contains=search)|Q(describe__contains=search))
        page = PagerObj(current_page, '/process/list/?search={}'.format(search),process_all, total_num)
        pager,process_list = page.pages()
    return render(request,'process/list.html',{"process_list":process_list,'pager': mark_safe(pager)})

@auth
def AddProcess(request):
    if request.method == 'GET':
        form = forms.ProcessName()
        user_list = User.objects.all()
        return render(request,'process/add.html',{"user_list":user_list,"form":form})

    if request.method == 'POST':
        form = forms.ProcessName()
        create_time = time.strftime('%Y-%m-%d %X')
        process_sorting = ''
        process_name = request.POST.get('process_name')
        describe = request.POST.get('describe')
        for i in request.POST:
            if i != "process_name" and i != "describe":
                if process_sorting:
                    process_sorting = process_sorting + ',' + i
                else:
                    process_sorting = i
        if process_sorting:
            process_add = process_models.Process.objects.create(name=process_name,process=process_sorting,describe=describe,create_time=create_time)
            if process_add:
                return redirect('/process/list/')
        else:
            error_msg = "添加失败！"
            return render(request,'process/add.html',{"error_msg":error_msg,"form":form})
    return render(request,'process/add.html')

@auth
def EditProcess(request):
    if request.method == 'GET':
        form = forms.ProcessName()
        id = request.path.split('/')[-2]
        process_obj = process_models.Process.objects.filter(id=id)
        process_user_id = process_obj.values('process')[0]['process']
        for i in process_obj:
            process_obj = i
        process_user_id_list = process_user_id.split(',')
        user_list_obj = []
        user_list = User.objects.all()
        for i in process_user_id_list:
            user_obj = User.objects.all().filter(id=i).all()
            for j in user_obj.values():
                user_list_obj.append(j)
            user_list = user_list.filter().exclude(id=i)
        return render(request, 'process/edit.html', {"user_list": user_list, "form": form,"process_obj":process_obj,'user_list_obj':user_list_obj})

    return render(request,'process/edit.html')

@auth
def SaveProcess(request):
    if request.method == 'POST':
        describe = request.POST.get('describe')
        id = request.POST.get('id')
        process_sorting = ''
        change_time = time.strftime('%Y-%m-%d %X')
        for i in request.POST:
            if i != "process_name" and i != "describe" and i != 'id':
                if process_sorting:
                    process_sorting = process_sorting + ',' + i
                else:
                    process_sorting = i
        process_obj = process_models.Process.objects.filter(id=id).update(process=process_sorting,change_time=change_time,describe=describe)
        if process_obj:
            return redirect('/process/list/')
        return redirect('/process/edit/%s/'.format(id))

@auth
def InfoPorcess(request):
    if request.method == 'GET':
        id = request.path.split('/')[-2]
        proce = UserProcessObj(id)
        process_obj,user_list_obj = proce.get_process_obj()

    return render(request,'process/info.html',{'process_obj':process_obj,'user_list_obj':user_list_obj})

@auth
def DeleteProcess(request):
    if request.method == 'POST':
        del_id = request.POST.get('id',0)
        if del_id:
            if not del_id:
                return redirect('/process/list/')
            if del_id.isdigit():
                del_process = process_models.Process.objects.filter(id=del_id).delete()
                return HttpResponse(json.dumps({'msg':'删除成功'}))
        else:
            del_id_lsit_obj = request.POST.lists()
            for i in del_id_lsit_obj:
                del_id_list = i[1]
            try:
                t = del_id_list
            except Exception  as e:
                return redirect('/process/list/')
            for del_id in del_id_list:
                del_process = process_models.Process.objects.filter(id=del_id).delete()
            return HttpResponse(json.dumps({'msg': '删除成功'}))
    return redirect('/process/list/')


@auth
def MyProcess(request):
    if request.method == 'GET':
        user_id = get_user_id(request.session['user'])
        current_page = int(request.GET.get('p', 1))
        option_process = request.GET.get('option_process_select','all')
        intermediate_obj = process_models.Intermediate.objects.all().filter(create_user_id=user_id)
        obj = OptionProcess(option_process,int(current_page),'/process/myprocess/',intermediate_obj)
        render_dict = obj.process_page()
        return render(request,'process/myprocess.html',render_dict)

@auth
def AllHistory(request):
    if request.method == 'GET':
        current_page = int(request.GET.get('p', 1))
        option_process = request.GET.get('option_process_select', 'all')
        intermediate_obj = process_models.Intermediate.objects.all()
        obj = OptionProcess(option_process, int(current_page), '/process/all/', intermediate_obj)
        render_dict = obj.process_page()

        return render(request,'process/all.html',render_dict)

@auth
def CreateProcess(request):
    if request.method == 'GET':
        form = forms.CreateUserProcessForm()
        process_all_obj = process_models.Process.objects.all()
        return render(request,'process/create.html',{"process_all_obj":process_all_obj,"form": form})

    if request.method == 'POST':
        create_user = get_user_id(request.session['user'])
        describe = request.POST.get('describe','')
        process_id = request.POST.get('select_process_id')
        file_obj = request.FILES.get('attachment','')
        create_name = request.POST.get('create_name')
        qualified_suffix_list = ['txt','jpg','png','doc','docx','xlsx','xls']
        suffix = str(file_obj).split('.')[-1]
        save_file = ''
        if file_obj:
            if suffix not in qualified_suffix_list:
                form = forms.CreateUserProcessForm()
                error_msg = '上传的附件格式不允许!'
                process_all_obj = process_models.Process.objects.all()
                return render(request,'process/create.html',{"process_all_obj":process_all_obj,"form": form,'error_msg':error_msg})
            save_dir = 'static/intermediate/'
            name = str(time.time()).replace('.','')+'.'+suffix
            save_file = save_dir + name
            with open(save_file,'wb+') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
        process_str = process_models.Process.objects.get(id=process_id).process
        audit_user = process_str.split(',')[0]
        create_time = time.strftime('%Y-%m-%d %X')
        add_intermediate = process_models.Intermediate.objects.create(name=create_name,describe=describe,attachment=save_file,process_str=process_str,user=audit_user,create_time=create_time,create_user_id=create_user,process_id=process_id)
        if add_intermediate:
            if settings.EAMIL:
                mail = ProcessMail()
                mail.send_notice(add_intermediate.id,request.get_host())
            return redirect('/process/list/')
        return redirect('/process/list/')

@auth
def AuditListProcess(request):
    if request.method == 'GET':
        user_id = get_user_id(request.session['user'])
        audit_all = process_models.Intermediate.objects.filter(user=user_id,status='0').all()
        return render(request,'process/audit_list.html',{'audit_all':audit_all})

@auth
def AuditInfoProcess(request):
    if request.method == 'GET':
        audit_user = get_user_id(request.session['user'])
        audit_id = int(request.GET.get('audit'))
        intermediate_obj = process_models.Intermediate.objects.filter(id=audit_id).all()
        if not intermediate_obj:
            return redirect('/process/audit/list/')
        if int(audit_user) != int(intermediate_obj.values('user')[0]['user']):
            return redirect('/process/audit/list/')
        for i in intermediate_obj:intermediate_obj = i
        proce = UserProcessObj(intermediate_obj.process_id)
        process_obj, user_list_obj = proce.get_process_obj()
        read_process(audit_user,audit_id)

        return render(request,'process/audit.html',{'intermediate_obj':intermediate_obj,'process_obj': process_obj, 'user_list_obj': user_list_obj})


@auth
def AuditProcess(request):
    if request.method == 'POST':
        user_id = get_user_id(request.session['user'])
        id = request.POST.get('id')
        status = request.POST.get('success')
        if not status:
            if settings.EAMIL:
                mail = ProcessMail()
                mail.send_failed(id,request.get_host())
            process_models.Intermediate.objects.filter(id=id).update(status='1')
            return redirect('/process/audit/list/')
        process_obj = process_models.Intermediate.objects.get(id=id)
        process_user = process_obj.user
        process_str = process_obj.process_str
        process_user_list = process_str.split(',')
        user_index_len = len(process_user_list)-1
        user_index = process_user_list.index(str(user_id))
        if int(process_user) != user_id:
            return HttpResponse(403)
        if int(user_index) == user_index_len:
            if settings.EAMIL:
                mail = ProcessMail()
                mail.send_notice(id,request.get_host())
            process_models.Intermediate.objects.filter(id=id).update(status='2')
            return redirect('/process/audit/list/')
        else:
            new_user_id = process_user_list[user_index+1]
            update_process = process_models.Intermediate.objects.filter(id=id).update(user=new_user_id)
            if update_process:
                set_read_process(user_id,id)
            if settings.EAMIL:
                mail = ProcessMail()
                mail.send_notice(id,request.get_host())
            return redirect('/process/audit/list/')

@auth
def DescribeProcess(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        describe_obj = process_models.Intermediate.objects.filter(id=id).all()
        for i in describe_obj:describe_obj = i
        if describe_obj:
            proce = UserProcessObj(int(describe_obj.process_id))
            process_obj, user_list_obj = proce.get_process_obj()
            return render(request,'process/describe.html',{'describe_obj':describe_obj,'process_obj':process_obj,'user_list_obj':user_list_obj})
        return HttpResponse('describe')


