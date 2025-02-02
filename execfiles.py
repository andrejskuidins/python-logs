import os
import sys
import logging
import subprocess

APP_LOG = "app.log"

logging.basicConfig(
  level = logging.INFO,
  handlers = [ logging.StreamHandler(),
  logging.FileHandler(APP_LOG)
  ]
)

def execfiles(path: str) -> None:
  try:
    with os.scandir(path) as it:
      for entry in it:
        if os.path.splitext(entry.name)[1] == ".sh" and entry.is_file():
            logging.info(f'executing file {entry.name}')
            subprocess.run(entry.path)
  except subprocess.SubprocessError as e:
    logging.error(f'execute error: {e}')
  except OSError as e:
    logging.error(f'os error: {e}')
  except ValueError as e:
    logging.error(f'value error: {e}')


def get_var() -> str:
  try:
    return sys.argv[1]
  except (IndexError, ValueError) as e:
    logging.error(e)
    sys.exit(1)

execfiles(get_var())