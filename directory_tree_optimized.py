"""
Directory tree processor - creates directories and executes shell scripts
based on a configuration file.
"""

import subprocess
import logging
import sys
from pathlib import Path
from typing import Iterator
import argparse

# Configuration file names for logging and processing
APP_LOG = "directory_tree.log"
APP_CONF = "directory_tree.conf"

#AI! how to refactor?
# Set up logging to output to both console and a log file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(APP_LOG)],
)
logger = logging.getLogger(__name__)


def read_config(config_file: str) -> Iterator[str]:
    """
    Yield non-empty lines from the configuration file.

    Args:
        config_file: Path to the configuration file.

    Yields:
        Stripped non-empty lines from the file.
    """
    try:
        with open(config_file, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    yield stripped
    except FileNotFoundError:
        logger.error("Configuration file not found: %s", config_file)
        raise
    except PermissionError:
        logger.error("Permission denied reading config file: %s", config_file)
        raise


def process_config(location: str, config_file: str = APP_CONF) -> None:
    """
    Process each line from the configuration file.
    For each path, check if it's a file or directory.
    Execute shell scripts and create directories at the specified location.

    Args:
        location: Base directory where new directories will be created.
        config_file: Path to the configuration file.
    """
    location_path = Path(location)

    for linux_obj in read_config(config_file):
        try:
            logger.info("Processing object: %s", linux_obj)
            path = Path(linux_obj)

            if path.is_file():
                execute_file(path)
            elif path.is_dir():
                check_create_dir(location_path, path)
            else:
                logger.warning("Not a valid file or directory: %s", linux_obj)

        except FileNotFoundError as e:
            logger.error("File not found: %s", e)
        except PermissionError as e:
            logger.error("Permission denied: %s", e)
        except OSError as e:
            logger.error("OS error processing %s: %s", linux_obj, e)
        except Exception as e:
            logger.error("Unexpected error processing %s: %s", linux_obj, e)


def check_create_dir(location: Path, source_dir: Path) -> None:
    """
    Create a directory at the specified location using the base name of the input path.
    If the directory already exists, no error will be raised.

    Args:
        location: Base directory where the new directory will be created.
        source_dir: Source directory path to extract the name from.
    """
    try:
        target_dir = location / source_dir.name
        logger.info("Creating directory: %s", target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logger.error("Cannot create directory %s: %s", target_dir, e)


def execute_file(file_path: Path) -> None:
    """
    Execute a shell script file if it has a .sh extension.
    Uses subprocess.run to run the script and capture its output.

    Args:
        file_path: Path to the file to potentially execute.
    """
    if file_path.suffix != ".sh":
        logger.debug("Skipping non-shell file: %s", file_path)
        return

    try:
        logger.info("Executing shell script: %s", file_path)
        result = subprocess.run(
            ["/bin/bash", str(file_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout:
            logger.debug("Script output: %s", result.stdout)
    except subprocess.CalledProcessError as e:
        logger.error("Script failed with exit code %d: %s", e.returncode, file_path)
        if e.stderr:
            logger.error("Script stderr: %s", e.stderr)
    except subprocess.SubprocessError as e:
        logger.error("Cannot execute script %s: %s", file_path, e)


def main() -> int:
    """
    Main function to parse command line arguments and start processing.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    parser = argparse.ArgumentParser(
        description="Create directories and execute shell scripts based on a config file."
    )
    parser.add_argument(
        "location",
        help="Base directory where new directories will be created."
    )
    parser.add_argument(
        "--config",
        "-c",
        default=APP_CONF,
        help=f"Path to configuration file (default: {APP_CONF})"
    )
    args = parser.parse_args()

    location_path = Path(args.location)
    if not location_path.exists():
        logger.error("Location does not exist: %s", args.location)
        return 1
    if not location_path.is_dir():
        logger.error("Location is not a directory: %s", args.location)
        return 1

    try:
        process_config(args.location, args.config)
        return 0
    except Exception as e:
        logger.error("Fatal error: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
