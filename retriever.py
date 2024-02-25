import requests
import time
import json

URL = "https://ipfs.io/ipfs/QmNQBifyRLitkRJkmEKr3zrsotYes9MUZkL8iAuhVwrmwU"

while True:
    print("Requesting ...")
    response = requests.get(URL)
    print(response)
    time.sleep(120)