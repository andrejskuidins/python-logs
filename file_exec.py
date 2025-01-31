import os
import subprocess

def parse_folder(dir):
    try:
        dir = os.path.expanduser(dir)
        for f in os.listdir(path=dir):
            full_path = os.path.join(dir, f)
            if os.path.isdir(full_path):
                print(f'Directory: {full_path}')
                for sub_f in os.listdir(path=dir):
                    print(f'- item{sub_f}')
            elif os.path.isfile(full_path):
                if f == "request_test.py":
                    print(f'File: {full_path}')
                    print(f'File: {f}')
                    try:
                        subprocess.run(["python3", full_path], check=True)
                    except subprocess.CalledProcessError as e:
                        print(f'Error executing file: {e}')
    except OSError as e:
        print(f'OS Error: {e}')
    except PermissionError as e:
        print(f'Permission: {e}')
    except Exception as e:
        print(f'Exception: {e}')

folder_name = "~/Documents/python-logs"
parse_folder(folder_name)