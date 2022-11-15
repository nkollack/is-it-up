#!/usr/bin/env python3
import urllib.request
from time import localtime, strftime, sleep
import os
from playsound import playsound


def internet_on():
    try:
        urllib.request.urlopen("http://google.com", timeout=1)
        return True
    except urllib.error.URLError as err:
        return False


def main():
    while not internet_on():
        print(f'Internet Unavailable: {strftime("%Y-%m-%d %I:%M:%S", localtime())}')
        sleep(60)
        os.system("cls")
    print("Internet Available")
    while True:
        playsound("./alert.mp3")
        sleep(2.1)


if __name__ == "__main__":
    main()
