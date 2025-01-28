from django.urls import path, include
from django.conf.urls import handler404
from errors import errors
from app.settings import DEVELOPMENT
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = errors.handler404

urlpatterns = [
  path('', include('whitelist.urls')),
  path('', include('documentation.urls')),
]

if DEVELOPMENT:
  urlpatterns += staticfiles_urlpatterns()