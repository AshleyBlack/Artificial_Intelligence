import requests
import json
import re
import csv

this_line = []
station_on_line = []
temp_array = []


with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(station_on_line)


class Stations:
    def __init__(self):
        self.code = None
        self.connections = []

    def add_code(self, code):
        self.code = code

    def add_connection(self, connection):
        self.connections.append(connection)


all_stations = []
i = 0
with open('norfolk_station_codes.csv', newline='') as norfolk_stations:
    stations_reader = csv.reader(norfolk_stations, delimiter=',')
    for row in stations_reader:
        station_obj = Stations()
        with open('routes.csv', newline='') as route_stations:
            route_reader = csv.reader(route_stations, delimiter=',')
            for route_row in route_reader:
                curr_station = str(row[0])
                station_obj.add_code(str(row[0]))
                if curr_station in route_row:
                    for items in route_row:
                        if items not in station_obj.connections and items is not '':
                            station_obj.add_connection(items)
       #print(station_obj.connections)
        all_stations.append(station_obj)
    for items in all_stations:
        if not items.connections:
            print(items.code)
            print(items.connections)




