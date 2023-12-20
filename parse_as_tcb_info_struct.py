import os, sys
import json


def parse_v4_api_v3_spec(data):
    assert(data['tcbInfo']['version'] == 3)
    return {
        'pceid': data['tcbInfo']['pceId'],
        'fmspc': data['tcbInfo']['fmspc'].lower(),
        'tcbLevels': [_parse_v4_api_v3_tcbLevels(level) for level in data['tcbInfo']['tcbLevels']],
    }

def _parse_v4_api_v3_tcbLevels(data):
    return {
        'pcesvn': data['tcb']['pcesvn'],
        'sgxTcbCompSvnArr': [component['svn'] for component in data['tcb']['sgxtcbcomponents']],
        'status': _parse_v3_status(data['tcbStatus']),
    }


def _parse_v3_status(status):
    return {
        "UpToDate": 0,
        "SWHardeningNeeded": 1,
        "ConfigurationAndSWHardeningNeeded": 2,
        "ConfigurationNeeded": 3,
        "OutOfDate": 4,
        "OutOfDateConfigurationNeeded": 5,
        "Revoked": 6,
    }.get(status, 0)

def parse_v4_api_data(data):
    return { fmspc.lower(): parse_v4_api_v3_spec(spec) for fmspc, spec in data.items() }

def write_to_asset_files(data):
    if not os.path.exists("assets"):
        os.mkdir("assets")
    for fmspc, spec in data.items():
        if not os.path.exists("assets/"+fmspc):
            os.mkdir("assets/"+fmspc)
        with open("assets/"+fmspc+"/tcbinfo.json", "w") as outfile:
            outfile.write(json.dumps(spec, indent=None, ensure_ascii=True))

write_to_asset_files(parse_v4_api_data(json.loads(sys.stdin.read())))
