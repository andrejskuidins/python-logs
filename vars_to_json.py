import requests
import json
import os
import sys

def launch_rest(env) -> None
    try:
        url = os.environ[env]
        r = requests.get(url)
        if r.status_code == 200:
            print("SUCCESS")
            print(r.json())
            with open("status.log", "w") as f:
                f.write(f'{json.dumps(r.json())}\n\n')
                f.write(r.text)
        else:
            print(r.status_code)
    except requests.exceptions.RequestException as e:
        print(f'Error occured: {e}')
    except ValueError as e:
        print(f'Parsing error: {e}')
    except KeyError as e:
        print(f'KeyError error: {e}')
        print(f'Processing from the argument')
        r = requests.get(sys.argv[1])
        print(r.json())

launch_rest("ENVMY")
