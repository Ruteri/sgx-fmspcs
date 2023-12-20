import requests
import json 
import sys

all_data = {}
all_fmpcs = json.loads(sys.stdin.read())
for spec in all_fmpcs:
    res = requests.get('https://api.trustedservices.intel.com/sgx/certification/v4/tcb?fmspc='+spec['fmspc']+'&update=early')
    all_data[spec['fmspc']] = json.loads(res.text)

print(json.dumps(all_data, indent=2))
