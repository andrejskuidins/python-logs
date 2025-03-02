import requests
import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

MERCHANT_URL = 'http://127.0.0.1:5000/merchants'
LOGGING_LOG = 'merchant.log'
PAYMENTS_OUT = 'payments.csv'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler(LOGGING_LOG)])

def merchant_processor(merchant: str) -> None:
    sum_amount = 0
    sum_fees = 0
    r = requests.get(f'{MERCHANT_URL}/{merchant}')
    for i in r.json()["transactions"]:
        sum_amount += i["amount"]
        sum_fees   += i["fee"]
    total_amount = (sum_amount - sum_fees)*(100-r.json()["discount"]["fees_discount"]/100)
    write_transactions(r.json()["iban"], total_amount)

def init_out_file() -> None:
    with open(PAYMENTS_OUT, "w") as f:
        f.write("iban,amount_in_pence\n")

def write_transactions(iban: str, amount: int) -> None:
    with open(PAYMENTS_OUT, "a") as f:
        f.write(f'{iban},{str(amount)}\n')

if __name__=="__main__":
    start_time = time.time()

    init_out_file()

    merchants = requests.get(MERCHANT_URL).json()

    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(merchant_processor, merchants)

    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    logging.info(f"Elapsed time: {elapsed_time:.6f} seconds")