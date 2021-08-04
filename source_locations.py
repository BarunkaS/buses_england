import urllib.request
import json
import pandas as pd
import os


# API key
bus_api_key = os.environ.get('BUS_TRACKING_APIKEY')


# APIs
locations_api = 'https://data.bus-data.dft.gov.uk/api/v1/datafeed/3439/?api_key='+str(bus_api_key)

t=2880

#for i in range(0,t):
response = urllib.request.urlopen(locations_api)
location_raw = pd.read_xml(response)

