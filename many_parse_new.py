import json

# 1. Better variable names
COMMON_DICT = {}

# 2. Added docstrings
def parse_json(json_file: str) -> dict:
    """Parse JSON log file into a dictionary with timestamp as key."""
    # 1. Better variable names
    result = {}
    with open(json_file, "r") as file:
        for line in file:
            # 1. Better variable names
            data = json.loads(line)
            result[data.get("timestamp")] = data.get("message")
    return result

# 2. Added docstrings
def parse_out(out_file: str) -> dict:
    """Parse syslog output file into a dictionary."""
    # 1. Better variable names
    result = {}
    with open(out_file, "r") as file:
        for line in file:
            # 1. Better variable names
            parts = line.split()
            # 3. Added safety check
            if len(parts) >= 4:
                result[parts[0]] = parts[3]
    return result

# 2. Added docstrings
def dict_iterator(json_dict: dict, out_dict: dict) -> None:
    """Find and store entries matching specific patterns from both dictionaries."""
    # 4. Improved readability with better parameter names
    # 5. More descriptive loop variable names
    # Find entries with "Eclipse" in message from JSON data
    for timestamp, message in json_dict.items():
        if "Eclipse" in message:
            # 5. Consistent naming
            COMMON_DICT[timestamp] = message
    
    # Find entries with "wl" in value from syslog data
    for key, value in out_dict.items():
        if "wl" in value:
            # 5. Consistent naming
            COMMON_DICT[key] = value
    
    print(COMMON_DICT)

if __name__ == "__main__":
    # 6. Better main execution
    json_data = parse_json("logging-0.json")
    out_data = parse_out("syslog_parsed.out")
    # 7. Formatting improvements
    dict_iterator(json_data, out_data)
