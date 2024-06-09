from django.urls import path, include
from django.conf.urls import handler404
from errors import errors

handler404 = errors.handler404

urlpatterns = [
  path('', include('whitelist.urls')),
  path('', include('documentation.urls')),
]