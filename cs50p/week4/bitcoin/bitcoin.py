import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests