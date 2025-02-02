import os
import subprocess

def exec_files(path):
  try:
    with os.scandir(path) as it:
      for entry in it:
        if os.path.splitext(entry.name)[1] == ".sh" and entry.is_file():
          print(f'{entry.path}')
          subprocess.run([entry.path])
  except subprocess.SubprocessError as e:
    print(f'Subprocess Error: {e}')
  except ValueError as e:
    print(f'Value Error: {e}')
  except Exception as e:
    print(f'Generic Error: {e}')

exec_files("/home/azur/Documents/python-logs")
