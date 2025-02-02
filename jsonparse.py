import json
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    handlers=[
                      logging.StreamHandler(),
                      logging.FileHandler('myapp.log', mode="a")
                      ]
                    )

def json_parse(filename: str) -> None:
  d = {}
  required = "m7xhUGu9SjKGXYxedjmpmA"
  first_param = "component"
  second_param = "cluster.uuid"
  json_parsed = "json_parsed.txt"
  try:
    with open(filename, 'r') as f_read:
      for line in f_read:
        if required in line:
          js = json.loads(line)
          d[js.get(first_param)] = js.get(second_param)
      logging.info(d)
    with open(json_parsed, 'w') as f_write:
      for key, value in d.items():
        f_write.write(f'{key} -> {value}\n')
  except json.JSONDecodeError as e:
    logging.error(f'json decode erorr: {e}')
  except FileNotFoundError as e:
    logging.error(f'bad file name: {e}')
  except Exception as e:
        logging.error(f'Unexpected error: {e}')

if __name__ == "__main__":
  if len(sys.argv) != 2:
    logging.error(f'usage: python jsonparse.py <filename>')
  else:
    json_parse(sys.argv[1])