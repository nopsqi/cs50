import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
if not sys.argv[1].is