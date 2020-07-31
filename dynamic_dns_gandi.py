import requests
import datetime
from config import *

headers = { 'Content-Type': 'application/json', 'Authorization': "Apikey {}".format(api_key)}
url = "https://api.gandi.net/v5/livedns/domains/{}/records/{}/{}".format(fqdn, rrset_name, rrset_type)
body = {"rrset_ttl": 10800, "rrset_values": ["24.255.70.235"]}
r = requests.put(url, headers=headers, json=body)


print("{}    ----    {}".format(datetime.datetime.now().strftime("%c"), r.text))
