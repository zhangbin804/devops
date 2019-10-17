from django.urls import path,re_path
from apps.operational import views

urlpatterns = [
    path('create/password/',views.CreatePassword),
    path('list/server/',views.ServerList),
    path('create/server/',views.CreateServer),
    re_path('read/server/\d+/',views.ReadServer),
    re_path('edit/server/\d+/',views.GetEditServer),
    path('edit/server/',views.PostEditServer),
    path('delete/server/',views.DeleteServer),
    path('create/group/',views.CreateGroup),
    path('delete/group/',views.DeleteGroup),
    path('list/group/',views.GroupList),
    re_path('edit/group/\d+/',views.GetEditGroup),
    path('edit/group/',views.PostEditGroup),
    re_path('read/group/\d+/',views.ReadGroup),
    path('server/list/user/',views.ListServerUser),
    path('server/create/user/',views.CreateServerUser),
    path('server/edit/user/',views.EditServerUser),
    path('server/delete/user/',views.DeleteServerUser),
    path('server/read/user/',views.ReadServerUser),

]
