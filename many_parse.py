import json
from typing import Dict, Any


def parse_json_file(json_file_path: str) -> Dict[str, str]:
    """Parse a JSON log file and extract timestamp-message pairs."""
    parsed_data = {}
    try:
        with open(json_file_path, "r") as file:
            for line in file:
                try:
                    entry = json.loads(line)
                    timestamp = entry.get("timestamp")
                    message = entry.get("message")
                    if timestamp is not None:
                        parsed_data[timestamp] = message
                except json.JSONDecodeError as e:
                    print(f"Warning: Could not parse line as JSON: {e}")
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        raise
    return parsed_data


def parse_out_file(out_file_path: str) -> Dict[str, str]:
    """Parse a space-separated output file and extract key-value pairs."""
    parsed_data = {}
    try:
        with open(out_file_path, "r") as file:
            for line in file:
                parts = line.split()
                if len(parts) >= 4:
                    parsed_data[parts[0]] = parts[3]
                else:
                    print(f"Warning: Line does not have enough parts: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: Output file '{out_file_path}' not found.")
        raise
    return parsed_data


def filter_and_merge_dicts(
    json_data: Dict[str, str],
    out_data: Dict[str, str]
) -> Dict[str, str]:
    """
    Filter both dictionaries based on content and merge them.
    Entries from json_data are included if their value contains 'Eclipse'.
    Entries from out_data are included if their value contains 'wl'.
    """
    result = {}

    # Filter json_data entries
    for key, value in json_data.items():
        if value and "Eclipse" in value:
            result[key] = value

    # Filter out_data entries
    for key, value in out_data.items():
        if value and "wl" in value:
            result[key] = value

    return result


def main() -> None:
    """Main function to execute the parsing and filtering."""
    try:
        json_data = parse_json_file("logging-0.json")
        out_data = parse_out_file("syslog_parsed.out")

        filtered_data = filter_and_merge_dicts(json_data, out_data)

        # Print the result
        print(filtered_data)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Program terminated due to error: {e}")


if __name__ == "__main__":
    main()
