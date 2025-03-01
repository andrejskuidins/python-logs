import requests
import logging
import time
from multiprocessing import Pool

MERCHANT_URL = 'http://127.0.0.1:5000/merchants'
LOGGING_LOG = 'merchant.log'
PAYMENTS_OUT = 'payments.csv'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler(LOGGING_LOG)])

def merchant_processor(url: str) -> None:
    with open(PAYMENTS_OUT, "w") as f:
        f.write("iban,amount_in_pence\n")
    merchants = requests.get(url)
    for i in merchants.json():
        get_merchant_trans(i.strip(), url)


def get_merchant_trans(merchant: str, url: str) -> str:
    sum_amount = 0
    sum_fees = 0
    r = requests.get(url + "/" + merchant)
    for i in r.json()["transactions"]:
        sum_amount += i["amount"]
        sum_fees   += i["fee"]
    write_transactions(r.json()["iban"], sum_amount - sum_fees)


def write_transactions(iban: str, amount: int) -> None:
    with open(PAYMENTS_OUT, "a") as f:
        f.write(iban + "," + str(amount) + "\n")

if __name__=="__main__":
    start_time = time.time()
    merchant_processor(MERCHANT_URL)
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    logging.info(f"Elapsed time: {elapsed_time:.6f} seconds")