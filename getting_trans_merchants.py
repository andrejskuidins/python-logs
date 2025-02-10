import requests
import json
import logging

logging(..............)

ULR_MERCH = 'https://simpledebit.gocardless.io/merchants'
TRANS_API = 'https://simpledebit.gocardless.io/merchants/'
PAYMENTS = 'payments.csv'

def get_api_mechants(url: str) -> None:
    r = requests.get(url)
    for i in r.json():
        try:
            get_api_transactions(i)
        except:


def get_api_transactions(merchant: str) -> None:
    try:
        full_api = TRANS_API + merchant
        r = requests.get(full_api)
        if r.status_code == 200:
            print(r.json()['transactions'])

            write_file(PAYMENTS, r.json()['id'], r.json()['iban'], transactions_calc(r.json()['transactions']))
        else:
            write_file("no response")
    except:

def transactions_calc(trans_list: list) -> int:
    calc_of_trans = 0
    for i in trans_list:
        calc_of_trans += int(i["amount"])
        calc_of_trans -= int(i["fee"])
    return calc_of_trans

def write_file(filename: str, id: str, iban: str, transactions: int) -> None:
    with open(filename, "a") as f:
        f.write(f'{iban},{str(transactions)}\n')

def main():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('filename')           # positional argument
    get_api_mechants(ULR_MERCH)


if __name__=="__main__":
    main()