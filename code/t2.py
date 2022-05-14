#!/usr/bin/python3

import boto3
import json
import requests
import sys
from os.path import basename

date = '2022-03-07'
bucket = 'jm3-airflow'
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=%s&api_key=DEMO_KEY' % date
max_imgs = 3

page = requests.get(url)
api_results = json.loads(page.text)

s3 = boto3.client('s3')

print( len(api_results['photos']))

sys.exit()

for x in api_results['photos'][0:max_imgs]:
  imgurl = x['img_src']
  imgfname = basename(imgurl)
  key = 'img/%s/%s' % (date,imgfname)
  print('Transferring %s' % imgurl)
  s3.put_object(Bucket=bucket, 
                Key=key,
                Body=requests.get(imgurl).content)

