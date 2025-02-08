import os
import subprocess

def get_list(config_file: str="directory_tree.conf") -> list:
    with open(config_file, "r") as f:
        for l in f:
            if os.is_file(l):
                execute_file(l)
            else:
                check_create_dir(l)

def check_create_dir(filename: str) -> None:
    os.makedirs(os.path.basename(filename), )

def execute_file(filename: str) -> None:
    if os.path.splitext(filename)[1] == ".sh"
        subprocess.run(filename)


get_list()