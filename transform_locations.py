import pandas as pd
from os.path import join, dirname
from dotenv import load_dotenv
from lxml import etree
from bs4 import BeautifulSoup
import boto3
import os
import glob

# loading keys
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
s3_access_key = os.environ.get("S3_ACCESS_KEY")
s3_secret_key = os.environ.get("S3_SECRET_KEY")

# s3 authentication
s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-2',
    aws_access_key_id=s3_access_key,
    aws_secret_access_key=s3_secret_key
)

# all location files
locations_files = glob.glob("40locations_files/*")

all_dataframes = []

for file in locations_files:
    location_data_raw = open(file, 'r').read()
    locations_html = etree.HTML(location_data_raw)
    prettified_locations_html = etree.tostring(locations_html, pretty_print=True, method="html")

    souped_html = BeautifulSoup(prettified_locations_html,features="lxml")

    #finding data
    # time of response
    response_timestamp=souped_html.find('responsetimestamp')

    #line data
    vehicle_activity=souped_html.find_all('vehicleactivity')

    parsed_activity=()
    locations_list=[]

    for activity in vehicle_activity:
        row_locations_list=[]
        parsed_activity=activity

        row_locations_list.append(activity.find('recordedattime').string)
        row_locations_list.append(activity.find('validuntiltime').string)
        row_locations_list.append(activity.find('lineref').string)
        row_locations_list.append(activity.find('vehicleref').string)
        row_locations_list.append(activity.find('blockref').string)
        row_locations_list.append(activity.find('latitude').string)
        row_locations_list.append(activity.find('longitude').string)

        locations_list.append(row_locations_list)

    # into a dataframe

    locations_dataframe = pd.DataFrame(locations_list, columns=[
                                                'recordedattime', 
                                                'validuntiltime',
                                                'lineref',
                                                'vehicleref',
                                                'blockref',
                                                'latitude',
                                                'longitude'
                                                ])

    all_dataframes.append(locations_dataframe)

all_location = pd.concat(all_dataframes, ignore_index=True)
print(all_location)

