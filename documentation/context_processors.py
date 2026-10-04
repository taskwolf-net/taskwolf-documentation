from app.settings import ENVIRONMENT

def domain(request):
  if ENVIRONMENT == 'PRODUCTIVE':
    domain = 'taskwolf.net'
    request_prefix = 'https://api.taskwolf.net/v1'
    public_endpoint = 'https://api.taskwolf.net'
  elif ENVIRONMENT == 'STAGING':
    domain = 'taskwolf.dev'
    request_prefix = 'https://api.taskwolf.dev/v1'
    public_endpoint = 'https://pub.taskwolf.dev'
  elif ENVIRONMENT == 'LOCAL':
    domain = 'taskwolf.dev'
    request_prefix = 'http://10.96.0.4/v1'
    public_endpoint = 'https://pub.taskwolf.dev'
  return {
    'domain': domain,
    'request_prefix': request_prefix,
    'public_endpoint': public_endpoint
  }