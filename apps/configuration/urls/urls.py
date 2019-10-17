from django.urls import path
from apps.configuration import views

urlpatterns = [
    path('edit/password/',views.EditPassword),
    path('edit/email/',views.EditEmail),
    path('edit/avatar/',views.EditAvatar),
]
