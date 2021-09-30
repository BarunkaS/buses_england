# in progress
import urllib
import json
import pandas as pd
import os


# API key
bus_api_key = os.environ.get('BUS_TRACKING_APIKEY')

# APIs
timetable_api = 'https://data.bus-data.dft.gov.uk/api/v1/dataset?offset=0&status=published&api_key='+str(bus_api_key)

# defined functions
# move to separate file upon completion
def opening_url(url):
    response = urllib.request.urlopen(url)
    json_response = json.loads(response.read()) 
    return pd.DataFrame.from_dict(json_response)

timetable_data = opening_url(timetable_api)

timetable_data.to_csv('timetable_data_published.csv',index=False,mode='w')


# note: response contains count - total amount of entries fulfilling that criteria, but the query returns max. limit 100(?)
# SO: to ge the full list have to iterate hrough the whole with setting offset and limit
