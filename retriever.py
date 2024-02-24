import requests
import time
import json

URL = "https://ipfs.io/ipfs/QmNyeG7EwT3EaHThuYuogPvhtJW8nMmzM1PwycipxwzHaF"

while True:
    print("Requesting ...")
    response = requests.get(URL)
    print(response)
    time.sleep(120)