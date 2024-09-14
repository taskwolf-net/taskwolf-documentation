from functools import wraps
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext

def documentation_page(function):
  @wraps(function)
  async def documentation_page(request, *args, **kwargs):
    applyLanguage(request)
    return await function(request, *args, **kwargs)
  return documentation_page

def applyLanguage(request):
  language = request.COOKIES.get("dulno-documentation-language")
  if (language is None):
    translation.activate("en")
  translation.activate(language)

@documentation_page
async def overview(request):
  return render(request, 'overview.html', {'title': gettext("documentation.overview.title"),
    'css': ['css/base/documentation-header.css', 'css/base/documentation-footer.css',
      'css/base/documentation-page-bar.css', 'css/base/documentation-content-bar.css',
      'css/documentation/overview.css']})

@documentation_page
async def changeLog(request):
  return render(request, 'change-log.html', {'title': gettext("documentation.change.log.title"),
    'css': ['css/base/documentation-header.css', 'css/base/documentation-footer.css',
      'css/base/documentation-page-bar.css', 'css/base/documentation-content-bar.css',
      'css/documentation/change-log.css']})

@documentation_page
async def apps(request):
  return render(request, 'apps.html', {'title': gettext("documentation.apps.title"),
    'css': ['css/base/documentation-header.css', 'css/base/documentation-footer.css',
      'css/base/documentation-page-bar.css', 'css/base/documentation-content-bar.css',
       'css/documentation/apps.css']})

@documentation_page
async def webhooks(request):
  return render(request, 'webhooks.html', {'title': gettext("documentation.webhooks.title"),
    'css': ['css/base/documentation-header.css', 'css/base/documentation-footer.css',
      'css/base/documentation-page-bar.css', 'css/base/documentation-content-bar.css',
      'css/documentation/webhooks.css']})

@documentation_page
async def glossary(request):
  return render(request, 'glossary.html', {'title': gettext("documentation.glossary.title"),
    'css': ['css/base/documentation-header.css', 'css/base/documentation-footer.css',
      'css/base/documentation-page-bar.css', 'css/base/documentation-content-bar.css',
      'css/documentation/glossary.css']})