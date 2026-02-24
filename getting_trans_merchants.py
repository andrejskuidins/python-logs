import requests
import argparse
import logging
import os
import sys
from typing import List, Dict, Any

URL_MERCH = 'https://simpledebit.gocardless.io/merchants'
TRANS_API = 'https://simpledebit.gocardless.io/merchants/'
PAYMENTS_LOG = 'payments.log'

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(PAYMENTS_LOG)
    ]
)


def write_file(filename: str, iban: str, transactions: int) -> None:
    with open(filename, "a") as f:
        f.write(f'{iban},{transactions}\n')


def transactions_calc(trans_list: List[Dict[str, Any]], discount: int) -> int:
    calc_of_amount = sum(int(t["amount"]) for t in trans_list)
    calc_of_fees = sum(int(t["fee"]) for t in trans_list)
    return round(calc_of_amount - calc_of_fees + calc_of_fees * discount / 100)


def get_api_transactions(session: requests.Session, merchant: str, filename: str) -> None:
    try:
        response = session.get(f"{TRANS_API}{merchant}")
        response.raise_for_status()
        data = response.json()
        write_file(
            filename,
            data['iban'],
            transactions_calc(data['transactions'], data['discount']['fees_discount'])
        )
    except requests.exceptions.RequestException as e:
        logging.error(f'Request error for merchant {merchant}: {e}')
    except (KeyError, ValueError) as e:
        logging.error(f'Data error for merchant {merchant}: {e}')
    except PermissionError as e:
        logging.error(f'Permission error: {e}')


def get_api_merchants(url: str, filename: str) -> None:
    if os.path.exists(filename):
        os.remove(filename)

    with requests.Session() as session:
        try:
            response = session.get(url)
            response.raise_for_status()
            merchants = response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Failed to fetch merchants: {e}')
            return
        except ValueError as e:
            logging.error(f'Invalid JSON response: {e}')
            return

        for merchant in merchants:
            try:
                get_api_transactions(session, merchant, filename)
            except Exception as e:
                logging.error(f'Unknown error processing merchant {merchant}: {e}')


def main():
    parser = argparse.ArgumentParser(
        description='Program captures merchants and calculates their balance with output to a file'
    )
    parser.add_argument('filename', nargs='?', default='payments.csv')
    args = parser.parse_args()
    get_api_merchants(URL_MERCH, args.filename)


if __name__ == "__main__":
    main()
