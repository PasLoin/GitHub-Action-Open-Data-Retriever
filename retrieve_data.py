#!/usr/bin/python3
"""This script calls the API to retrieve the data and dumps into a file."""
import requests
from datetime import datetime
import os
import csv

# Format the name of the output file
FMT = "%Y-%m-%d-%H-%M"
FOLDER_PATH = "./history"
time = datetime.now()
filename = f'history_{time.strftime(FMT)}.csv'

# Following link to understand the API functionnalities
# cf. https://data.mobility.brussels/bike/api/counts/
# nrows=-1 means we will retrieve all the stations
# https://data.mobility.brussels/bike/api/counts/
URL = "https://data.mobility.brussels/bike/api/counts/?request=history&featureID=CJM90&startDate=20211201&endDate=20221231&outputFormat=csv"
response = requests.get(URL)
# print(f"{'Successful' if response.status_code == 200 else 'Unsuccessful'} call to the API") 
data = response.text()
# print("Size of the response: ", len(data['records']))
with open(f'{FOLDER_PATH}/{filename}', 'w') as output:
    csv.dump(data["records"], output)
