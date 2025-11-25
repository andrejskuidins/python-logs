import os
import requests
import logging
from typing import Dict, Any
import ast

LOGGING_LOG = "out.log"
RESULT_LOG = "result.log"
URL = "http://127.0.0.1:5000/merchants"
logging.basicConfig(
    handlers=[logging.FileHandler(LOGGING_LOG), logging.StreamHandler()],
    level=logging.INFO,
)


def find_rich(filename: str) -> Dict[str, int]:
    with open(filename, "r") as f:
        current = {"merchant": "", "total_amount": 0}
        for line in f:
            merch_data = ast.literal_eval(line.strip())
            sum_value = merch_data["total_amount"]
            if sum_value > current["total_amount"]:
                current = merch_data
    return current


def get_mechant_trans(merchant: str) -> Dict[str, Any]:
    r = requests.get(f"{URL}/{merchant}")
    # logging.info(r.json()["transactions"])
    total_amount = 0
    for t in r.json()["transactions"]:
        total_amount += t["amount"]
        total_amount -= t["fee"]
    return {"merchant": merchant, "total_amount": total_amount}


def main():
    r = requests.get(URL)
    for m in r.json():
        with open(RESULT_LOG, "a") as f:
            f.write(str(get_mechant_trans(m)) + "\n")
    print(find_rich(RESULT_LOG))


if __name__ == "__main__":
    main()
