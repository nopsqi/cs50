import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(f"{(response.json()["bpi"]["USD"] * number):,}")