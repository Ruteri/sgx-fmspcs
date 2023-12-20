import requests
import json 

res = requests.get('https://api.trustedservices.intel.com/sgx/certification/v4/fmspcs')
print(json.dumps(json.loads(res.text), indent=2))
