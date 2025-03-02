import logging
import time
import sys
from typing import List
from concurrent.futures import ProcessPoolExecutor

import requests

MERCHANT_URL = 'http://127.0.0.1:5000/merchants'
LOGGING_LOG = 'merchant.log'
PAYMENTS_OUT = 'payments.csv'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler(LOGGING_LOG)])

def merchant_processor(merchant: str) -> None:
    try:
        sum_amount = 0
        sum_fees = 0
        r = requests.get(f'{MERCHANT_URL}/{merchant}')
        if r.status_code == 200:
            data = r.json()
            for i in data["transactions"]:
                sum_amount += i["amount"]
                sum_fees   += i["fee"]
            total_amount = round(sum_amount - sum_fees)
            write_transactions(data["iban"], total_amount)
        else:
            logging.error(f'Merchant {merchant} has status code: {r.status_code}')
    except Exception as e:
        logging.error(f'Error processing merchant {merchant}: {e}')

def init_out_file() -> None:
    with open(PAYMENTS_OUT, "w") as f:
        f.write("iban,amount_in_pence\n")

def write_transactions(iban: str, amount: int) -> None:
    with open(PAYMENTS_OUT, "a") as f:
        f.write(f'{iban},{str(amount)}\n')

def main() -> None:
    start_time = time.time()

    init_out_file()

    try:
        merchants: List[str] = requests.get(MERCHANT_URL).json()
    except requests.exceptions.RequestException as e:
        logging.error(f'GoC servers are unavaiable: {e}')
        sys.exit(1)
    except ValueError as e:
        logging.error(f'Invalid JSON response: {e}')
        sys.exit(1)

    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(merchant_processor, merchants)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    logging.info(f"Elapsed time: {elapsed_time:.6f} seconds")

if __name__=="__main__":
    main()