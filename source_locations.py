from urllib import request
import os
from os.path import join, dirname
from dotenv import load_dotenv
import boto3
import time


# loading keys
dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)
bus_api_key = os.environ.get("BUS_TRACKING_APIKEY")
s3_access_key = os.environ.get("S3_ACCESS_KEY")
s3_secret_key = os.environ.get("S3_SECRET_KEY")

# APIs
locations_api = 'https://data.bus-data.dft.gov.uk/api/v1/datafeed/3439/?api_key='+str(bus_api_key)

# s3 authentication
s3 = boto3.resource(
    service_name='s3',
    region_name='eu-west-2',
    aws_access_key_id=s3_access_key,
    aws_secret_access_key=s3_secret_key
)

# runtime in minutes (specify in t) and rounds
#t=2880

t=20
rounds=t*2

# saving raw files
#saving on local for devpt purposes only
for i in range(0,rounds):
    file_name='location'+str(i)+'.txt'
    f = open(file_name, 'w')
    locations_response = request.urlopen(locations_api)
    raw_locations = locations_response.read().decode('utf-8')
    f.writelines(raw_locations)
    print(f)
    s3.Bucket('buslocations').upload_file(Filename=file_name, Key='s3_'+file_name) # filename is the original file name, key is the name it will have in S3
    f.close()
##    os.remove(file_name)
    time.sleep(30)
