.PHONY: assets
assets: full_fmspcs_data.json
	cat full_fmspcs_data.json | python3 parse_as_tcb_info_struct.py

full_fmspcs_data.json: available_fmspcs.json
	cat available_fmspcs.json | python3 fetch_fmspcs_data.py >full_fmspcs_data.json

available_fmspcs.json:
	python3 fetch_available_fmspcs.py > available_fmspcs.json
