from django.urls import path, include
from . import documentation

urlpatterns = [
  path('', documentation.overview),
  path('overview/', documentation.overview),
]