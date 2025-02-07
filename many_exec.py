import os
import subprocess
import logging
import argparse

APP_LOG = 'many_exec.log'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),logging.FileHandler(APP_LOG)])

def exec_file(filename: str) -> int:
    try:
        subprocess.run(filename, timeout=20, capture_output=True)
    except subprocess.CalledProcessError as e:
        logging.error(f'process ended abnormally: {e}')
    except Exception as e:
        logging.error(f'Generic error: {e}')

def list_dir_find_sh(path: str) -> str:
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.name.endswith('.sh') and entry.is_file():
                    exec_file(entry.path)
    except OSError as e:
        logging.error(f'list directory error: {e}')
    except TypeError as e:
        logging.error(f'no such directory: {e}')
    except Exception as e:
        logging.error(f'Generic error: {e}')

def main():
    parser = argparse.ArgumentParser(
                        prog='ProgramExecutor',
                        description='Exec files',
                        epilog='For non-production use')
    parser.add_argument('dirname')           # positional argument
    args = parser.parse_args()
    list_dir_find_sh(args.dirname)

if __name__=="__main__":
    main()