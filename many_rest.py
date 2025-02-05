import requests
import logging
import sys
import json

RESPONSE_CODE_LOG = 'response_code.log'
RESPONSE_CODE_TXT = 'response_code.txt'

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


def write_to_file(json: str, file: str=RESPONSE_CODE_TXT, ) -> None:
    try:
        with open(file, "a") as f:
            logging.info(f'Logging following reply: {json}')
            f.write(f'{json}\n')
    except OSError as e:
        logging.error(f'Operating system error: {e}')


def many_requests(amount: int=5) -> None:
    for i in range(amount):
        try:
            get_api(sys.argv[1])
        except Exception as e:
            logging.error(f'Generic exception: {e}')

if __name__=="__main__":
    if len(sys.argv) == 2:
        many_requests()
    elif len(sys.argv) == 3:
        try:
            amount = int(sys.argv[2])
            many_requests(amount)
        except ValueError as e:
            logging.error("Correct usage: many_rest.py <api_url> <num_retry>")
    else:
        logging.error("Correct usage: many_rest.py <api_url> <num_retry>")

