import json

def get_json(filename) -> list:
    try:
        f = open(filename, 'r', encoding="utf-8")
        c = 0
        l = []
        for line in f:
            c += 1
            print(f'{line.strip()} - number {c}')
            l.append(c)
    except FileExistsError:
        print("File does not exist")


file="workfile.txt"
get_json(file)