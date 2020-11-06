"""
Dashboard urls
"""
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('users.urls')),
    url('^admin/', admin.site.urls),
]
