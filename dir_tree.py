import os
import logging
import subprocess

DIR_PARSE_LOG = "dir.log"
FILENAME = "directory_tree.conf"


def read_file(filename):
    with open(filename, "r") as f:
        for line in f:
            cmd = line.rstrip("\n")
            if os.path.splitext(cmd)[1] == ".sh":
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True)
                    logging.info(result.stdout)
                except FileNotFoundError as e:
                    logging.error(f"kindy create file: {cmd}")
                except PermissionError as e:
                    logging.error(f"kindy adjust chmod: {cmd}")
            else:
                logging.info(cmd)


def main():
    os.remove(DIR_PARSE_LOG)
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler(), logging.FileHandler(DIR_PARSE_LOG)],
        format="%(message)s",
    )
    read_file(FILENAME)


if __name__ == "__main__":
    main()
