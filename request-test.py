import requests
import json

def get_response(path) -> bool:
    try:
        r = requests.get(path).json()
        print(r.get('status'))

        f = open('workfile.txt', 'a', encoding="utf-8")
        f.write(f'%s\n' % json.dumps(r))
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except ValueError as json_err:
        print(f"JSON parsing error: {json_err}")

url="https://simpledebit.gocardless.io/health_check"
get_response(url)