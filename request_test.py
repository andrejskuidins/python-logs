import requests
import json

def get_response(path) -> bool:
    try:
        r = requests.get(path)
        r_json = r.json()
        print(r_json.get('status'))
        if r.status_code == 200:
            print("SUCCESS")

        f = open('workfile.txt', 'a', encoding="utf-8")
        f.write(f'{json.dumps(r_json)}\n')
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except ValueError as json_err:
        print(f"JSON parsing error: {json_err}")

url="https://simpledebit.gocardless.io/health_check"
get_response(url)