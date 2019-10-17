from django.urls import path
from apps.accounts import views

urlpatterns = [
    path('',views.Index),
    path('index/',views.Index),
    path('login/',views.Login.as_view()),
    path('logout/',views.Logout),
    path('delete/navigation/',views.DeleteNavigation),
    path('add/navigation/',views.AddNavigation),
    path('change/page/',views.ChangePage),
    path('403.html',views.permission_denied),
]

