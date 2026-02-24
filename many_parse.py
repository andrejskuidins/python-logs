#AI! refactor using best practices
import json

DICT_COMMON = {}

def parse_json(json_file: str) -> dict:
    jdict = {}
    with open(json_file, "r") as f:
        for l in f:
            j = json.loads(l)
            jdict[j.get("timestamp")] = j.get("message")
    return jdict

def parse_out(out_file: str) -> dict:
    odict = {}
    with open(out_file, "r") as f:
        for l in f:
            j = l.split()
            odict[j[0]] = j[3]
    return odict

def dict_iterator(d1: dict, d2: dict) -> None:
    for k,v in d1.items():
        if "Eclipse" in v:
            DICT_COMMON[k] = v
    for k,v in d2.items():
        if "wl" in v:
            DICT_COMMON[k] = v
    print(DICT_COMMON)

if __name__=="__main__":
    dict_iterator(parse_json("logging-0.json"), parse_out("syslog_parsed.out"))
