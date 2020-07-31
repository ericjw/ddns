import requests
import sys
import os
from datetime import datetime
import time
from config import *



headers = { 'Content-Type': 'application/json', 'Authorization': "Apikey {}".format(api_key)}
url = "https://api.gandi.net/v5/livedns/domains/{}/records".format(fqdn)
body = {"items": [{"rrset_name" :a_name, "rrset_ttl": 10800, "rrset_type": "A", "rrset_values": ["24.255.70.235"]}]}
r = requests.put(url, headers=headers, json=body)

# print(r.request)
# print(r.status_code)
print(r.text)
