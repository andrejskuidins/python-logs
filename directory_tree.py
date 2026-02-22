import os
import subprocess
import logging
import argparse

APP_LOG = "directory_tree.log"
APP_CONF = "directory_tree.conf"

logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler(), logging.FileHandler(APP_LOG)]
)


def get_list(location, config_file: str = APP_CONF) -> list:
    with open(config_file, "r") as f:
        for l in f:
            try:
                linux_obj = l.strip()
                logging.info("Processing object: %s", linux_obj)
                if os.path.isfile(linux_obj):
                    execute_file(linux_obj)
                elif os.path.isdir(linux_obj):
                    check_create_dir(location, linux_obj)
                else:
                    logging.info("Not suitable object %s", linux_obj)
            except FileNotFoundError as e:
                logging.error("file %s doesnt exist", e)
            except PermissionError as e:
                logging.error("user %s doesnt have access", e)
            except Exception as e:
                logging.error("unexpected exception: %s", e)


def check_create_dir(location: str, dirname: str) -> None:
    try:
        logging.info("Creating dirs: %s", dirname)
        os.makedirs(f"{location}/{os.path.basename(dirname)}", exist_ok=True)
    except OSError as e:
        logging.error("cannot create directory due to error: %s", e)


def execute_file(filename: str) -> None:
    try:
        if os.path.splitext(filename)[1] == ".sh":
            logging.info("Executing file: %s", filename)
            subprocess.run(filename, capture_output=True)
    except subprocess.SubprocessError as e:
        logging.error("cannot run process due to error: %s", e)


def main():
    parser = argparse.ArgumentParser(
        description="Program capturs files and folders and executes files while creating folders"
    )
    parser.add_argument("location")  # positional argument
    args = parser.parse_args()
    try:
        get_list(args.location)
    except Exception as e:
        logging.error(f"Unexpected error in main execution: {e}")


if __name__ == "__main__":
    main()
