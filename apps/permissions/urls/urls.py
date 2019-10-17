from django.urls import path,re_path
from apps.permissions import views

urlpatterns = [
    path('list/',views.ListPermissions),
    re_path('edit/\d+/',views.EditPermissions),
    path('list/user/',views.ListUser),
    re_path('edit/user/\d+/',views.EditUser),
    path('delete/user/',views.DeleteUser),
    path('disable/user/',views.DisableUser),
    path('create/user/',views.CreateUser),
    path('create/roles/',views.CreateRoles),
    path('delete/roles/',views.DeleteRoles),
    path('change/permissions/',views.ChangePermissions),


]