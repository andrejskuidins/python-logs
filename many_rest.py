import requests
import logging
import sys
import json
import argparse

RESPONSE_CODE_LOG = 'response_code.log'
RESPONSE_CODE_TXT = 'response_code.txt'
DEFAULT_RETRIES = 5

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(RESPONSE_CODE_LOG)
    ])


def get_api(path: str) -> None:
    try:
        r = requests.get(path)
        if r.status_code == 200:
            write_to_file(json.dumps(r.json()))
        else:
            logging.error(f'Received non-200 status code: {r.status_code} for URL: {path}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Problem with http: {e}')


def write_to_file(json_data: str, file: str=RESPONSE_CODE_TXT, ) -> None:
    try:
        with open(file, "a") as f:
            logging.info(f'Logging following reply: {json_data}')
            f.write(f'{json_data}\n')
    except OSError as e:
        logging.error(f'Operating system error: {e}')


def many_requests(amount: int=DEFAULT_RETRIES) -> None:
    for i in range(amount):
        try:
            get_api(sys.argv[1])
        except Exception as e:
            logging.error(f'Generic exception: {e}')

def main():
    parser = argparse.ArgumentParser(description="Fetch data from an API endpoint.")
    parser.add_argument("url", help="The URL of the API endpoint.")
    parser.add_argument(
        "retries", nargs="?", type=int, default=DEFAULT_RETRIES,
        help="Number of retries (default: 5)."
    )
    args = parser.parse_args()

    many_requests(args.retries)

if __name__ == "__main__":
    main()
