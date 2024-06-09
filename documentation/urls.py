from django.urls import path, include
from . import documentation

urlpatterns = [
  path('', documentation.overview),
  path('overview/', documentation.overview),
  path('change-log/', documentation.changeLog),
  path('apps/', documentation.apps),
  path('webhooks/', documentation.webhooks),
  path('glossary/', documentation.glossary),
]