import subprocess
import logging
from pathlib import Path
import argparse

# Configuration file names for logging and processing
APP_LOG = "directory_tree.log"
APP_CONF = "directory_tree.conf"

# Set up logging to output to both console and a log file
logging.basicConfig(
    level=logging.INFO, handlers=[logging.StreamHandler(), logging.FileHandler(APP_LOG)]
)


# AI! make optimizations to code
def get_list(location, config_file: str = APP_CONF) -> list:
    """
    Process each line from the configuration file.
    For each path, check if it's a file or directory.
    Execute shell scripts and create directories at the specified location.
    """
    with open(config_file, "r") as f:
        for line in f:
            try:
                linux_obj = line.strip()
                if not linux_obj:
                    continue
                logging.info("Processing object: %s", linux_obj)
                path = Path(linux_obj)
                if path.is_file():
                    execute_file(linux_obj)
                elif path.is_dir():
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
    """
    Create a directory at the specified location using the base name of the input path.
    If the directory already exists, no error will be raised.
    """
    try:
        logging.info("Creating dirs: %s", dirname)
        target_dir = Path(location) / Path(dirname).name
        target_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logging.error("cannot create directory due to error: %s", e)


def execute_file(filename: str) -> None:
    """
    Execute a shell script file if it has a .sh extension.
    Uses subprocess.run to run the script and capture its output.
    """
    try:
        if Path(filename).suffix == ".sh":
            logging.info("Executing file: %s", filename)
            subprocess.run(filename, capture_output=True)
    except subprocess.SubprocessError as e:
        logging.error("cannot run process due to error: %s", e)


def main():
    """
    Main function to parse command line arguments and start processing.
    Expects a location argument where directories will be created.
    """
    parser = argparse.ArgumentParser(
        description="Program captures files and folders and executes files while creating folders"
    )
    parser.add_argument("location")  # positional argument
    args = parser.parse_args()
    try:
        get_list(args.location)
    except Exception as e:
        logging.error(f"Unexpected error in main execution: {e}")


if __name__ == "__main__":
    main()
