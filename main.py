import threading
import requests
import colorama
import time
import logging
import os

from time import sleep
from colorama import Fore
from threading import Thread

os.system("title solo.to checker")

logging.basicConfig(
    level=logging.INFO,
    format=f"{Fore.CYAN}[{Fore.RESET} %(asctime)s {Fore.CYAN}]{Fore.RESET}%(message)s",
    datefmt="%H:%M:%S"
)

usernames = open("usernames.txt", "r").read().splitlines()

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def solo(username):
    r = requests.get(f"https://solo.to/{username}", headers=headers)

    if r.status_code == 404:
        logging.info(f" {Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} is Available or Banned: solo.to/{username}")
        with open("hits.txt", "a") as file:
            file.write("solo.to/" + username + "\n")

    elif r.status_code == 200 or 204:
        logging.info(f" {Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Taken: solo.to/{username}")

    elif r.status_code == 409:
        logging.info(f" {Fore.RED}[{Fore.RESET}!{Fore.RED}]{Fore.RESET} Ratelimited: wait — 60 seconds")
        time.sleep(60)

threads = []

for username in usernames:
    threads.append(Thread(target=solo, args=[username]))

for x in threads:
    x.start()

for x in threads:
    x.join()