from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'blogApp/', include('blogApp.urls', namespace='blogApp', app_name='blogApp')),
]