import requests

def call_url(path) -> None:
  r = requests.get(path)
  print(r.status_code)


call_url("https://simpledebit.gocardless.io/health_check")