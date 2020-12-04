import os
import sys

import requests
from dotenv import load_dotenv


def import_data(day):
    ID = os.getenv("SESSION_ID")
    url = f"https://adventofcode.com/2020/day/{day}/input"

    cookies = {
        'session': os.getenv('SESSION_ID'),
    }

    res = requests.get(url, cookies=cookies)
    data = res.content.decode('UTF-8')
    return data


if __name__ == "__main__":
    day = sys.argv[1]
    filename = sys.argv[2]

    load_dotenv()
    data = import_data(day)

    if len(day) == 1:
        day = f"0{day}"

    try:
        os.mkdir(f"Day_{day}")
    except OSError as error:
        pass

    fi = open(f"Day_{day}/{filename}.txt", 'w')
    print(data, file=fi)
