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
except requests.RequestException:
    sys.exit("Failed to fetch BTC price")

print(f"${(response.json()['bpi']['USD']['rate_float'] * number):,.4f}")