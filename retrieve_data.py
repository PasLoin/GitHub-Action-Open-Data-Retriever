#!/usr/bin/python3
"""This script calls the API to retrieve the data and dumps into a file."""
import requests
from datetime import datetime
import os
import json

# Format the name of the output file
FMT = "%Y-%m-%d-%H-%M"
FOLDER_PATH = "./history"
time = datetime.now()
filename = f'history_{time.strftime(FMT)}.json'

# Following link to understand the API functionnalities
# cf. https://data.mobility.brussels/bike/api/counts/
# nrows=-1 means we will retrieve all the stations
# https://data.mobility.brussels/bike/api/counts/
URL = "https://data.opendatasoft.com/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel%40parisdata&facet=overflowactivation&facet=creditcard&facet=kioskstate&facet=station_state&rows=-1"
response = requests.get(URL)
# print(f"{'Successful' if response.status_code == 200 else 'Unsuccessful'} call to the API") 
data = response.json()
# print("Size of the response: ", len(data['records']))
with open(f'{FOLDER_PATH}/{filename}', 'w') as output:
    json.dump(data["records"], output)
