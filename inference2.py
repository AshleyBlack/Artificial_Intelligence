import requests
import json
import re
import csv

api_url = "https://hsp-prod.rockshore.net/api/v1/serviceMetrics"
details_api_url = "https://hsp-prod.rockshore.net/api/v1/serviceDetails"

headers = {"Content-Type": "application/json"}
email = 'Kieran.woodcock.93@gmail.com'
password = 'K13/s23/a3'
auths = (email, password)
station_on_line = []
# TODO: Narrow down list if possible
terminus = ['HFE', 'STN', 'LST', 'CBG', 'SMN', 'SOV', 'BTR', 'CLT', 'NRW', 'PBO', 'KLN', 'SHM', 'HWC', 'FLX', 'WON',
            'CET', 'SUY', 'BSE', 'SNF', 'IPS', 'ELY', 'GYM', 'TOM', 'HWN', 'BIS', 'LWT', 'CHN']
temp_array = []
i=1;

for station in terminus:
    print("Updating all routes from: " + station + " " + str(i) + "/" + str(len(terminus)))
    i = i + 1
    for other_station in terminus:
        data = {
            "from_loc": station,
            "to_loc": other_station,
            "from_time": "0900",
            "to_time": "1000",
            "from_date": "2018-07-01",
            "to_date": "2018-08-01",
            "days": "SATURDAY"
        }

        r = requests.post(api_url, headers=headers, auth=auths, json=data)
        text = json.dumps(json.loads(r.text), sort_keys=True, indent=2, separators=(',', ': '))
        print(text)