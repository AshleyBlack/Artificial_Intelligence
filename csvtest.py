import csv
import re
import requests
import json
import time

regex = re.compile('[^a-zA-Z]')
norfolk_stations = []
writer = open("lines.csv", "w")
api_url = "https://hsp-prod.rockshore.net/api/v1/serviceMetrics"
# api_url = "https://hsp-prod.rockshore.net/api/v1/serviceDetails"

headers = { "Content-Type": "application/json" }
email = 'Kieran.woodcock.93@gmail.com'
password = 'K13/s23/a3'
auths = (email, password)
route = ['a','b']
routes = []
origin_required = False
found_route = False
stations = []

class routes():
    def __init__(self, name, number_of_stations, stations):
        self.name = name
        self.number_of_stations = number_of_stations
        self.stations = stations

with open('norfolk_station_codes.csv', newline='') as depart:
    stations_reader = csv.reader(depart, delimiter=',')
    for row in stations_reader:
        stations.append(row)
found_route = False

for arrival in stations:
    print(arrival[0])
    found_route = False
    for depart in stations:
        if found_route:
            continue
        print(str(depart[0]))

        data = {
            "from_loc": depart[0],
            "to_loc": arrival[0],
            "from_time": "0800",
            "to_time": "0900",
            "from_date": "2018-10-05",
            "to_date": "2018-10-08",
            "days": "SATURDAY"
        }
        r = requests.post(api_url, headers=headers, auth=auths, json=data)
        if 'destination_location' in str(r.text):
            text = json.dumps(json.loads(r.text), sort_keys=True, indent=2, separators=(',', ''))
            lines = iter(text.splitlines())
            for line in lines:
                if not origin_required and re.match("(.*)destination(.*)", line):
                    route[0] = line
                    origin_required = True
                elif origin_required and re.match("(.*)origin(.*)", line):
                    route[1] = line
                    origin_required = False
                    found_route = True
                    print(route)
                    if route not in routes:
                        routes.append(route)
                        writer.write(str(route) + '\n')
                    break




