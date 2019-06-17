from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(r'^admin/', admin.site.urls),
    path(r'blogApp/', include(('blogApp.urls', 'blogApp'),namespace='blogApp'))
]