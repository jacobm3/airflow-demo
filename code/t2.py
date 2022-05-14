#!/usr/bin/python3

import boto3
import json
import requests
from os.path import basename

date = '2022-05-08'
bucket = 'jm3-airflow'
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=%s&api_key=DEMO_KEY' % date

page = requests.get(url)
api_results = json.loads(page.text)

s3 = boto3.client('s3')

for x in api_results['photos']:
  imgurl = x['img_src']
  imgfname = basename(imgurl)
  key = 'img/%s/%s' % (date,imgfname)
  s3.put_object(Bucket=bucket, 
                Key=key,
                Body=requests.get(imgurl).content)

