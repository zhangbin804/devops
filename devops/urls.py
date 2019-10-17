from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.accounts.urls.urls')),
    path('configuration/',include('apps.configuration.urls.urls')),
    path('process/',include('apps.process.urls.urls')),
    path('operational/',include('apps.operational.urls.urls')),
    path('permissions/',include('apps.permissions.urls.urls')),
    path('project/',include('apps.project.urls.urls')),

]
