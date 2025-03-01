import requests
import logging

MERCHANT_URL = 'https://simpledebit.gocardless.io/merchants'
LOGGING_LOG = 'merchant.log'

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.StreamHandler(),
                              logging.FileHandler(LOGGING_LOG)])

def get_merchant_list(MERCHANT_URL: str=MERCHANT_URL) -> None:
    r = requests.get(MERCHANT_URL)
    with open('merchant_list.config', 'w') as f:
        logging.info(r.json())
        f.write(str(r.json()))
    for merchant in r.json():
        get_all_transactions(merchant)

def get_all_transactions(merchant: str) -> None:
    r = requests.get(MERCHANT_URL +'/'+ merchant)
    with open('merchant_tans.config', 'a') as f:
        f.write(str(r.json()) + ',')

if __name__=="__main__":
    get_merchant_list()