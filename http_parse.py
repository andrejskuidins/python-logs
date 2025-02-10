import requests
import argparse
import logging

HTTP_PARSE_LOG='http_parse.log'
HTTP_PARSE_OUT='http_parse.out'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler(HTTP_PARSE_LOG)])

def write_to_file(filename: str, text: str) -> None:
    try:
        with open(filename, 'a') as f:
            f.write(text)
    except (OSError, PermissionError) as e:
        logging.error(f'Exception with file: {e}')

def get_api(count: int, url: str) -> None:
    for i in range(int(count)):
        try:
            r = requests.get(url)
            if r.status_code == 200:
                logging.info('writing to a file')
                write_to_file(HTTP_PARSE_OUT, r.text)
            else:
                logging.info(f'problem with api, executing curl {e}')
        except requests.exceptions.RequestException as e:
            logging.error(f'Exception with api: {e}')

def main() -> None:
    parser = argparse.ArgumentParser(description='Calls API and parses the out. Then writes all required data to a file')
    parser.add_argument('count', nargs='?', default=1)
    parser.add_argument('api_url', nargs='?', default="https://simpledebit.gocardless.io/health_check")
    args = parser.parse_args()

    try:
        get_api(args.count, args.api_url)
    except Exception as e:
        logging.error(f'Generic exception occured: {e}')

if __name__=="__main__":
    main()