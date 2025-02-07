import os
import subprocess
import logging
import argparse

APP_LOG = 'many_exec.log'
IMPORTANT_LOG = 'syslog_parsed.log'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),logging.FileHandler(APP_LOG)])

def exec_file(filename: str) -> int:
    try:
        e = subprocess.run(filename, timeout=20, capture_output=True, text=True)
        parse_write_to_file(IMPORTANT_LOG, e.stdout)
        if e.stderr:
            logging.info(e.stderr)
    except subprocess.CalledProcessError as e:
        logging.error(f'process ended abnormally: {e}')
    except Exception as e:
        logging.error(f'Generic error: {e}')

def parse_write_to_file(logname: str, buffer: str) -> None:
    lines = buffer.splitlines()
    matching_lines = [line for line in lines if "wezfurlong" in line]
    if matching_lines:
        with open(logname, 'w') as f:
            f.write("\n".join(matching_lines))

def list_dir_find_sh(path: str) -> str:
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.name.endswith('.sh') and entry.is_file():
                    logging.info(f'executing file: {entry.name}')
                    exec_file(entry.path)
    except OSError as e:
        logging.error(f'list directory error: {e}')
    except TypeError as e:
        logging.error(f'no such directory: {e}')
    except Exception as e:
        logging.error(f'Generic error: {e}')

def main():
    parser = argparse.ArgumentParser(description='Exec files')
    parser.add_argument('dirname')           # positional argument
    args = parser.parse_args()
    list_dir_find_sh(args.dirname)

if __name__=="__main__":
    main()