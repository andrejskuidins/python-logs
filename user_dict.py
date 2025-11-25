import requests
import logging
import os
import urllib3

urllib3.disable_warnings()

HTTP_PARSE_LOG = "employees.log"
HTTP_PARSE_OUT = "employees.out"


def clear_obsolete(file_out, file_log):
    try:
        os.remove(file_out)
        os.remove(file_log)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))


def get_user_email(name) -> None:
    url_path = f"https://localhost/api/users/{name}?user=andy"
    logging.info(f"Sending to: {url_path}")
    r = requests.get(
        url_path,
        auth=("andy", "pass"),
        verify=False,
    )
    logging.info(r.status_code)
    with open(HTTP_PARSE_OUT, "a") as f:
        try:
            f.write(r.json()["email"] + "\n")
        except KeyError as e:
            logging.error(f"No user within DB")


def main() -> None:
    clear_obsolete(HTTP_PARSE_LOG, HTTP_PARSE_OUT)
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.FileHandler(HTTP_PARSE_LOG), logging.StreamHandler()],
    )
    while True:
        logging.info("Kindly input username: ")
        username = input()
        get_user_email(username)


if __name__ == "__main__":
    main()
