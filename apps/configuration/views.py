from django.shortcuts import render, HttpResponse, redirect
from apps.permissions.init_permission import init_permission
from apps.accounts.forms.forms import ChangePasswordForm,ChangeEmailForm
from django.views import View
from apps.accounts.core.accounts_auth import auth,get_user_id
from apps.accounts.forms import forms
import time,os
from apps.permissions import models as permissions_models

@auth
def EditPassword(request):
    user = request.session['user']
    if request.method == 'GET':
        form = forms.ChangePasswordForm()
        return render(request,'configuration/password.html',{"form":form})
    if request.method == 'POST':
        form = forms.ChangePasswordForm(request.POST)
        if form.is_valid():
            old_password = form.clean()["old_password"]
            new_password1 = form.clean()['new_password']
            new_password2 = form.clean()['new_password2']
            if new_password1 != new_password2:
                error_msg = '2次密码不一致'
                form = forms.ChangePasswordForm()
                return render(request, 'configuration/password.html', {"form": form,'error_msg':error_msg})

            passwd = permissions_models.User.objects.filter(username=user,password=old_password).first()
            if passwd:
                permissions_models.User.objects.filter(username=user).update(password=new_password1)
                return redirect('/logout/')
            else:
                error_msg = '当前密码错误'
                form = forms.ChangePasswordForm()
                return render(request, 'configuration/password.html', {"form": form,'error_msg':error_msg})
@auth
def EditEmail(request):
    user = request.session['user']
    if request.method == 'GET':
        form = forms.ChangeEmailForm()
        old_email = permissions_models.User.objects.filter(username=user).values('email')[0]['email']
        return render(request,'configuration/email.html',{'form':form,'old_email':old_email})
    
    if request.method == 'POST':
        form = forms.ChangeEmailForm(request.POST)
        if form.is_valid():
            new_email = form.clean()['email']
            change_email = permissions_models.User.objects.filter(username=user).update(email=new_email)
            return redirect('/')

@auth
def EditAvatar(request):
    user = request.session['user']
    if request.method == 'GET':
        form = forms.EditAvatar()
        return render(request, 'configuration/avatar.html',{'form':form})
    if request.method == 'POST':
        file_obj = request.FILES.get('avatar')
        suffix = str(file_obj).split('.')[-1]
        qualified_suffix_list = ['jpg','png','JPG','PNG']
        save_file = ''
        if file_obj:
            if suffix not in qualified_suffix_list:
                form = forms.CreateUserProcessForm()
                error_msg = '上传的格式不允许!'
                return render(request,'configuration/avatar.html',{'error_msg':error_msg})
            save_dir = 'static/avatar/'
            name = str(time.time()).replace('.', '')
            save_file = save_dir + name + '.' + 'jpg'
            save_avatar_jpg = save_dir + name + '_avatar.' + 'jpg'
            with open(save_file,'wb+') as f:
                for chunk in file_obj.chunks():
                    f.write(chunk)
            import PIL.Image as image
            img = image.open(save_file)
            avatar_img = img.resize((150,150))
            avatar_img.save(save_avatar_jpg)
            os.remove(save_file)
            permissions_models.User.objects.filter(username=user).update(head_img=save_avatar_jpg)
            request.session["avatar"] = permissions_models.User.objects.filter(username=user).values('head_img')[0]['head_img']
            return redirect('/')

