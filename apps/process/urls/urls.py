from django.urls import path,re_path
from apps.process import views

urlpatterns = [
    path('list/',views.ListProcess),
    re_path('add/',views.AddProcess),
    re_path('delete/',views.DeleteProcess),
    re_path('edit/\d+/',views.EditProcess),
    path('save/', views.SaveProcess),
    re_path('info/\d+/',views.InfoPorcess),
    path('create/',views.CreateProcess),
    path('myprocess/',views.MyProcess),
    path('all/',views.AllHistory),
    path('audit/list/',views.AuditListProcess),
    path('audit/info/',views.AuditInfoProcess),
    path('audit/auth/',views.AuditProcess),
    path('describe/',views.DescribeProcess),
]
