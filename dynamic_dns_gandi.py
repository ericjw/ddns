import requests
import datetime
from config import *

ip = requests.get('https://api.ipify.org').text # get public IP
headers = { 'Content-Type': 'application/json', 'Authorization': "Apikey {}".format(api_key)}
url = "https://api.gandi.net/v5/livedns/domains/{}/records/{}/{}".format(fqdn, rrset_name, rrset_type)
body = {"rrset_ttl": ttl, "rrset_values": [ip]}

r = requests.put(url, headers=headers, json=body)


# logging
print("{}    ----    {}".format(datetime.datetime.now().strftime("%c"), r.text))
