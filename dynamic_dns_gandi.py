import requests
import sys
import os
from datetime import datetime
import time
from config import *



headers = { 'Content-Type': 'application/json', 'Apikey': api_key}
url = "https://api.gandi.net/v5/livedns/domains/{}/records".format(fqdn)
body = {"rrset_ttl": 10800, "rrset_type": "A", "rrset_values": ["xx.xx.xx.xx"]}
r = requests.put(url, headers=headers, data=body)

# print(r.request)
# print(r.status_code)
# print(r.text)