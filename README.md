# ddns
Use Gandi LiveDNS API to update a single DNS record with a dynamic IP.

### Prerequisites
- Gandi account and domain
- Gandi Production API key from user security settings
- Python 3.X

### Running
- Complete the config.py file:
```python
fqdn = "example.com" 
api_key = "abc123" 
rrset_name = "@" # name of the record to update
rrset_type = "A" # type of record to update
ttl = 10800 # the time in seconds that DNS resolvers should cache this record

```
- Run with 
```
python dynamic_dns_gandi.py
```

- Use cron to schedule ddns update:  
Edit your cron jobs with ```crontab -e``` and then paste the following into the file to run the python script every 5 minutes:  
```*/5 * * * * python3 ~/ddns/dynamic_dns_gandi.py >> ~/ddns/cronjob.log 2>&1```
