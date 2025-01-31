import json

def get_json(filename) -> list:
    try:
        f = open(filename, 'r', encoding="utf-8")
        c = 0
        for line in f:
            c += 1
            msg = json.loads(line.strip()).get('message')
            if "UMAlXDR8QQOtqaSE7NTubw" in msg:
                print(f'{msg}')
    except FileExistsError:
        print("File does not exist")


file="elasticsearch-logging-0.log"
get_json(file)