import requests
import logging
from typing import Dict, Any, List

LOGGING_LOG = "out.log"
URL = "http://127.0.0.1:5000/merchants"
logging.basicConfig(
    handlers=[logging.FileHandler(LOGGING_LOG), logging.StreamHandler()],
    level=logging.INFO,
)


def calculate_merchant_net_amount(merchant: str) -> Dict[str, Any]:
    """Calculate the net amount for a merchant by summing amounts and subtracting fees."""
    try:
        response = requests.get(f"{URL}/{merchant}")
        response.raise_for_status()
        data = response.json()
        
        total_amount = 0
        for transaction in data.get("transactions", []):
            total_amount += transaction.get("amount", 0)
            total_amount -= transaction.get("fee", 0)
        return {"merchant": merchant, "total_amount": total_amount}
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching transactions for merchant {merchant}: {e}")
        return {"merchant": merchant, "total_amount": 0}


def find_richest_merchant(merchant_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Find the merchant with the highest total_amount from a list of merchant data."""
    if not merchant_data:
        return {"merchant": "", "total_amount": 0}
    
    richest = merchant_data[0]
    for data in merchant_data[1:]:
        if data["total_amount"] > richest["total_amount"]:
            richest = data
    return richest


def main() -> None:
    """Main function to fetch all merchants, calculate their net amounts, and find the richest."""
    try:
        response = requests.get(URL)
        response.raise_for_status()
        merchants = response.json()
        
        if not isinstance(merchants, list):
            logging.error("Unexpected response format: expected a list of merchants")
            return
        
        merchant_results = []
        for merchant in merchants:
            result = calculate_merchant_net_amount(merchant)
            merchant_results.append(result)
            logging.info(f"Processed merchant: {merchant}")
        
        richest = find_richest_merchant(merchant_results)
        print(f"The richest merchant is {richest['merchant']} with total amount: {richest['total_amount']}")
        
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching merchant list: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
