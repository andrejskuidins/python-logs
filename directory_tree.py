#!/usr/bin/env python3
import os

def restore_directory_tree(paths, target_base_path):
    for path in paths:
        path = path.strip()
        if not path:
            continue

        full_target_path = os.path.normpath(os.path.join(target_base_path, path.lstrip('/')))

        if path.endswith('/'):
            os.makedirs(full_target_path, exist_ok=True)
            print(f"Created directory: {full_target_path}")
        else:
            os.makedirs(os.path.dirname(full_target_path), exist_ok=True)
            open(full_target_path, 'a').close()
            print(f"Created empty file: {full_target_path}")

PATHS = [
    '/temp/file1.c',
    '/var/file.ext',
    '/root/www/files/',
    '/home/user/projects/',
    '/var/log/myapp/debug.log'
]

restore_directory_tree(PATHS, '/tmp/restored')
