import os
import subprocess
import logging

APP_LOG = 'directory_tree.log'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),
                    logging.FileHandler(APP_LOG)])

def get_list(config_file: str="directory_tree.conf") -> list:
    with open(config_file, "r") as f:
        for l in f:
            if os.path.isfile(l):
                execute_file(l)
            elif os.path.isdir(l):
                check_create_dir(l)
            else:
                logging.info('Not suitable object')

def check_create_dir(dirname: str) -> None:
    os.makedirs(os.path.basename(dirname), )

def execute_file(filename: str) -> None:
    if os.path.splitext(filename)[1] == ".sh":
        subprocess.run(filename)


get_list()


