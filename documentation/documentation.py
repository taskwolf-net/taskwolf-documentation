from functools import wraps
from functools import partial
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import translation
from django.utils.translation import gettext

def home_page(function):
  @wraps(function)
  async def home_page(request, *args, **kwargs):
    applyLanguage(request)
    return await function(request, *args, **kwargs)
  return home_page

def applyLanguage(request):
  language = request.COOKIES.get("taskwolf-documentation-language")
  if (language is None):
    translation.activate("en")
  translation.activate(language)

@home_page
async def overview(request):
  return render(request, 'overview.html', {'title': gettext("documentation.overview.title"),
    'css': ['css/base/documentation-header.css', 'css/base/documentation-footer.css', 'css/documentation/overview.css']})