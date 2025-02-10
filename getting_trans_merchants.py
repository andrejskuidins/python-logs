import requests
import argparse
import logging
import os

ULR_MERCH = 'https://simpledebit.gocardless.io/merchants'
TRANS_API = 'https://simpledebit.gocardless.io/merchants/'
PAYMENTS_LOG = 'payments.log'


logging.basicConfig(level=logging.INFO,
                    handlers=[
                        logging.StreamHandler(),
                        logging.FileHandler(PAYMENTS_LOG)
                    ])



def write_file(filename: str, iban: str, transactions: int) -> None:
    with open(filename, "a") as f:
        f.write(f'{iban},{str(transactions)}\n')

def transactions_calc(trans_list: list, discount: int) -> int:
    calc_of_trans = 0
    for i in trans_list:
        calc_of_trans += int(i["amount"])
        calc_of_trans -= int(i["fee"])
    return round(calc_of_trans*(discount/100))

def get_api_transactions(merchant: str, filename: str) -> None:
    try:
        full_api = TRANS_API + merchant
        r = requests.get(full_api)
        if r.status_code == 200:
            write_file(filename, r.json()['iban'], transactions_calc(r.json()['transactions'], r.json()['discount']['fees_discount']))
        else:
            write_file("no response")
    except PermissionError as e:
        logging.error(f'Permission error: {e}')

def get_api_mechants(url: str, filename: str) -> None:
    r = requests.get(url)
    if os.path.exists(filename):
        os.remove(filename)
    for i in r.json():
        try:
            get_api_transactions(i, filename)
        except Exception as e:
            logging.error(f'Unknown error: {e}')

def main():
    parser = argparse.ArgumentParser(description='Program captures merchants and calculates heir balance with otput to a file payments.csv')
    parser.add_argument('filename', nargs='?', default='payments.csv')
    args = parser.parse_args()
    get_api_mechants(ULR_MERCH, args.filename)

if __name__=="__main__":
    main()
