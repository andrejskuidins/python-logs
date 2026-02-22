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
    results = []
    try:
        with open(config_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        logging.error("Configuration file '%s' not found", config_file)
        return results
    except PermissionError:
        logging.error("Permission denied when trying to read configuration file '%s'", config_file)
        return results
    except OSError as e:
        logging.error("OS error occurred while reading configuration file '%s': %s", config_file, e)
        return results
    
    for line_num, line in enumerate(lines, 1):
        try:
            linux_obj = line.strip()
            if not linux_obj:
                logging.debug("Skipping empty line %d", line_num)
                continue
                
            logging.info("Processing object: %s (line %d)", linux_obj, line_num)
            
            if os.path.isfile(linux_obj):
                execute_file(linux_obj)
                results.append(f"Executed file: {linux_obj}")
            elif os.path.isdir(linux_obj):
                check_create_dir(location, linux_obj)
                results.append(f"Created/checked directory: {linux_obj}")
            else:
                logging.warning("Object '%s' at line %d is neither a file nor a directory", linux_obj, line_num)
                results.append(f"Skipped: {linux_obj}")
                
        except FileNotFoundError:
            logging.error("Object '%s' at line %d not found", linux_obj, line_num)
            results.append(f"File not found: {linux_obj}")
        except PermissionError:
            logging.error("Permission denied for object '%s' at line %d", linux_obj, line_num)
            results.append(f"Permission denied: {linux_obj}")
        except OSError as e:
            logging.error("OS error for object '%s' at line %d: %s", linux_obj, line_num, e)
            results.append(f"OS error: {linux_obj}")
        except subprocess.SubprocessError as e:
            logging.error("Subprocess error for object '%s' at line %d: %s", linux_obj, line_num, e)
            results.append(f"Subprocess error: {linux_obj}")
        except Exception as e:
            logging.error("Unexpected error processing object '%s' at line %d: %s", linux_obj, line_num, e)
            results.append(f"Unexpected error: {linux_obj}")
    
    return results


def check_create_dir(location: str, dirname: str) -> None:
    try:
        target_dir = os.path.join(location, os.path.basename(dirname))
        logging.info("Creating directory: %s", target_dir)
        os.makedirs(target_dir, exist_ok=True)
        logging.info("Directory '%s' created or already exists", target_dir)
    except OSError as e:
        logging.error("Cannot create directory '%s' due to error: %s", 
                     os.path.join(location, os.path.basename(dirname)), e)
        raise  # Re-raise to be caught by the caller


def execute_file(filename: str) -> None:
    try:
        if os.path.splitext(filename)[1] == ".sh":
            logging.info("Executing shell script: %s", filename)
            # Check if the file is executable
            if not os.access(filename, os.X_OK):
                logging.warning("File '%s' is not executable. Attempting to make it executable.", filename)
                os.chmod(filename, os.stat(filename).st_mode | 0o111)
            
            result = subprocess.run(
                [filename],
                capture_output=True,
                text=True,
                timeout=30  # Add a timeout to prevent hanging
            )
            if result.returncode != 0:
                logging.error("Script '%s' exited with non-zero code %d: %s", 
                             filename, result.returncode, result.stderr)
            else:
                logging.info("Script '%s' executed successfully. Output: %s", 
                            filename, result.stdout[:100])  # Log first 100 chars
        else:
            logging.warning("File '%s' is not a shell script (.sh), skipping execution", filename)
    except subprocess.TimeoutExpired:
        logging.error("Script '%s' execution timed out after 30 seconds", filename)
    except subprocess.SubprocessError as e:
        logging.error("Subprocess error while executing '%s': %s", filename, e)
    except OSError as e:
        logging.error("OS error while executing '%s': %s", filename, e)
    except Exception as e:
        logging.error("Unexpected error while executing '%s': %s", filename, e)


def main():
    parser = argparse.ArgumentParser(
        description="Program captures files and folders and executes files while creating folders"
    )
    parser.add_argument("location", help="Target location for directory operations")
    args = parser.parse_args()
    
    # Validate the location exists or can be created
    if not os.path.exists(args.location):
        try:
            os.makedirs(args.location, exist_ok=True)
            logging.info("Created target location: %s", args.location)
        except OSError as e:
            logging.error("Cannot create target location '%s': %s", args.location, e)
            return
    
    try:
        results = get_list(args.location)
        logging.info("Processing completed. %d items processed.", len(results))
        for result in results:
            logging.debug("Result: %s", result)
    except Exception as e:
        logging.error("Unexpected error in main execution: %s", e)


if __name__ == "__main__":
    main()
