import requests
import json
import logging
import os
import sys

logging.basicConfig(
  level=logging.INFO,
  handlers=[
    logging.StreamHandler(),
    logging.FileHandler('app.log')
    ]
)

def call_url(path: str) -> None:
  try:
    r = requests.get(path)
    with open('workfile.txt', 'a') as f:
      f.write(f'{json.dumps(r.json())}\n')
      logging.info(r.status_code)
      logging.info(r.json())
  except requests.exceptions.RequestException as e:
    logging.error(f'Requests error: {e}')
  except ValueError as e:
    logging.error(f'Json error: {e}')
  except Exception as e:
    logging.error(f'Generic error: {e}')

def get_os_var() -> str:
  try:
    url=os.getenv(sys.argv[1])
    return url
  except (IndexError, ValueError) as e:
    logging.error(e)
    sys.exit(1)

call_url(get_os_var())
