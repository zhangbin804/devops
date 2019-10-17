from django.urls import path,re_path
from apps.project import views

urlpatterns = [
    path('list/',views.ListProject),
    path('create/',views.CreateProject),
    path('edit/',views.EditProject),
    path('read/',views.ReadProject),
    path('delete/',views.DeleteProjetc),
    path('release/',views.UpdateProject),
    path('rollback/',views.RollbackProject),
    path('tag/',views.GetTag),
    path('connection/test/',views.ConnectionTestAuth),

]
