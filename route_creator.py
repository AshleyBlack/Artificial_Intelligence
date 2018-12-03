import requests
import json
import re
import csv

# Documentation can be found at
#   https://wiki.openraildata.com/index.php/HSP

# When registering at https://datafeeds.nationalrail.co.uk/
# you only need the HSP subscription
# The Real time Data feed is too much to deal with
# The On Demand Data Feeds might be useful
#
# In 'Planned usage', mention you are using the HSP data
# for educational purposes, for a project, and for a limited
# time
# The T & Cs should not be an issue, nor the limit on the
# number of requests an hour - but do be polite and do not
# swamp the web service with an excessive number of requests

api_url = "https://hsp-prod.rockshore.net/api/v1/serviceMetrics"
details_api_url = "https://hsp-prod.rockshore.net/api/v1/serviceDetails"

headers = {"Content-Type": "application/json"}
email = 'Kieran.woodcock.93@gmail.com'
password = 'K13/s23/a3'
auths = (email, password)
station_on_line = []
# TODO: Narrow down list if possible
terminus = ['HFE', 'STN', 'LST', 'CBG', 'SMN', 'SOV', 'BTR', 'CLT', 'NRW', 'PBO', 'KLN', 'SHM', 'HWC', 'HPQ', 'FLX',
            'WON', 'CET', 'SUY', 'BSE', 'SNF', 'IPS', 'ELY', 'GYM', 'TOM', 'HWN', 'BIS', 'LWT', 'CHN']
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
            "to_time": "1200",
            "from_date": "2018-25-11",
            "to_date": "2018-27-11",
            "days": "MONDAY"
        }

        r = requests.post(api_url, headers=headers, auth=auths, json=data)
        text = json.dumps(json.loads(r.text), sort_keys=True, indent=2, separators=(',', ': '))
        lines = iter(text.splitlines())
        print_next = False
        for line in lines:
            if print_next:
                # print(line)
                print_next = False
                rid = re.sub("[^0-9]", "", line)
                data = {
                    "rid": rid
                }
                r = requests.post(details_api_url, headers=headers, auth=auths, json=data)
                text = json.dumps(json.loads(r.text), sort_keys=True, indent=2, separators=(',', ': '))
                detail_lines = iter(text.splitlines())
                # print(text)
                list_test = []
                for detail_line in detail_lines:
                    if re.match("(.*)location\"(.*)", detail_line):
                        temp = re.sub("[^A-Z]", "", detail_line)
                        temp = list(temp.split("[^A-Z"))
                        for item in temp:
                            list_test.append(item)
                        if list_test not in station_on_line:
                            station_on_line.append(list_test)
                break

            if 'rids' in line:
                print_next = True

with open("routes.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(station_on_line)
