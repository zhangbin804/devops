from django.shortcuts import render, HttpResponse, redirect
from apps.permissions.init_permission import init_permission
from apps.accounts.core.accounts_auth import auth,get_user_id
from apps.accounts.forms import forms
from django.views import View
from apps.accounts.models import *
from apps.permissions import models as permissions_models

@auth
def Index(request):
    if request.method == 'GET':
        user_id = get_user_id(request.session.get('user'))
        form = forms.AddNavigationForm()
        navigation_obj = Navigation.objects.filter(name=user_id).all()
        return render(request,'index.html',{'form':form,'navigation_obj':navigation_obj})

@auth
def AddNavigation(request):
    if request.method == 'POST':
        navigation_dict = {}
        navigation_dict['name_id'] = get_user_id(request.session.get('user'))
        navigation_dict['website_name'] = request.POST.get('website_name')
        navigation_dict['website_url'] = request.POST.get('website_url')
        add_website = Navigation.objects.create(**navigation_dict)
        return redirect('/index/')

@auth
def DeleteNavigation(request):
    if request.method == 'POST':
        website_lists = request.POST.lists()
        website_list = []
        for i in website_lists:
            website_list.append(i[0])
        for i in  website_list:
            delete_website = Navigation.objects.filter(id=i).delete()
        return redirect('/index/')


class Login(View):
    def get(self, request):
        form = forms.LoginUserForm()
        return render(request, 'login.html',{"form":form})

    def post(self, request):
        form = forms.LoginUserForm(request.POST)
        if form.is_valid():
            username = form.clean()["username"]
            password = form.clean()["password"]
            auth_user = permissions_models.User.objects.filter(name=username, password=password)
            if auth_user.first():
                if auth_user.values('disable')[0]['disable'] == 1:
                    msg = '账号被禁用'
                    return render(request, 'login.html', {'msg': msg, "form": form})
                init_permission(auth_user.first(), request)

                return redirect('/index/')
            else:
                msg = '账号或密码错误'
                return render(request, 'login.html', {'msg': msg,"form":form})


@auth
def Logout(request):
    if request.method == 'GET':
        del request.session["is_login"]
        return redirect('/login/')


@auth
def ChangePage(request):
    if request.method == 'GET':
        referer1 = str(request.META['HTTP_REFERER']).split('//')[-1]
        referer = '/'+referer1.split('/',1)[-1]
        page = request.GET.get('change_page')
        request.session["total_num"] = int(page)
        if referer:
            return redirect(referer)
        return redirect('/')

def permission_denied(request):
    return render(request,'403.html')
