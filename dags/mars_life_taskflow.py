import base64
import boto3
import botocore
import hvac
import json
import logging
import os
import re
import requests
import time
from os.path import basename

from datetime import datetime, timedelta
from airflow.decorators import dag, task # DAG and task decorators for interfacing with the TaskFlow API
from airflow.operators.python import get_current_context

boto_config = botocore.config.Config(region_name='us-east-1')
bucket = 'jm3-airflow'

@dag(
    dag_id='mars_life_taskflow_v42',
    # This defines how often your DAG will run, or the schedule by which your DAG runs. In this case, this DAG
    # will run every 30 mins
    schedule_interval=timedelta(days=1),
    # This DAG is set to run for the first time on January 1, 2021. Best practice is to use a static
    # start_date. Subsequent DAG runs are instantiated based on scheduler_interval
    start_date=datetime(2022, 4, 1),
    # When catchup=False, your DAG will only run for the latest schedule_interval. In this case, this means
    # that tasks will not be run between January 1, 2021 and 30 mins ago. When turned on, this DAG's first
    # run will be for the next 30 mins, per the schedule_interval
    catchup=True,
    max_active_runs=3,
    tags=['nasa','mars','aws','aws:rekognition','aws:s3']) # If set, this tag is shown in the DAG view of the Airflow UI


def mars_life_dag():
    """
    ### ETL Dag
    """

    @task()
    def NASA_API_get_mars_img_list():
        """Load 1 day of Mars images to s3. Return list of img URLs"""

        # Get logical execution date
        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        # Retrieve NASA API key
        vault_client = hvac.Client(verify=False)
        vault_resp = vault_client.secrets.kv.v2.read_secret_version(path='airflow/nasa') 
        nasa_api_key = vault_resp['data']['data']['api_key']

        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=%s&api_key=%s' % (date,nasa_api_key)
        max_imgs = 5

        response = requests.get(url)
        api_results = json.loads(response.text)

        logging.info('NASA response: %s' % api_results)

        img_list = []
        for x in api_results['photos'][0:max_imgs]:
            img_list.append(x['img_src'])

        return img_list


    @task()
    def S3_put_images(img_list: list):
        """Save list of img URLs to s3. Return list of object keys."""

        # Get logical execution date
        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        logging.info('S3_put_images() img_list=%s' % str(img_list))

        s3 = boto3.client('s3')

        key_list = []

        if len(img_list) == 0:
            logging.info('No results from api for %s' % date)
            key = 'img/%s/%s' % (date,'no-results.html')
            #key_list.append(key)
            s3.put_object(Bucket=bucket, Key=key, Body='Empty list from API on %s.' % date)
        else:
            for imgurl in img_list:
                imgfname = basename(imgurl)
                key = 'img/%s/%s' % (date,imgfname)
                key_list.append(key)
                logging.info('Transferring %s' % imgurl)
                s3.put_object(Bucket=bucket, Key=key, ACL='public-read', 
                    ContentDisposition='inline', ContentType='image/jpeg',
                    Body=requests.get(imgurl).content)

            # insert positive test samples
            psamples = ['FLB_705202199EDR_F0943386FHAZ00200M_pos1.JPG',
                        'FLB_705462902EDR_F0950370FHAZ00302M_pos2.JPG',
                        'FLB_704924623EDR_F0943086FHAZ00302M_pos3.JPG']
            br = boto3.resource('s3')
            for sample in psamples:
                source = {'Bucket': bucket, 'Key': 'positive-samples/%s' % sample}
                dest = br.Bucket(bucket)
                key = 'img/%s/%s' % (date,sample)
                dest.copy(source, key)
                key_list.append(key)

        return key_list

    @task()
    def Rekognition_detect_objects(key_list: list):
        """Perform Rekognition object detection on list of s3 objects. Store detections in s3 tags."""

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        logging.info('Rekognition_detect_objects(): key_list=%s' % str(key_list))

        rekog = boto3.client('rekognition', config=boto_config)
        s3 = boto3.client('s3')

        life_labels = [ 'animal', 'arachnid', 'face', 'female', 'horse', 'human',
            'insect', 'invertebrate', 'male', 'mammal', 'man', 'people', 'person',
            'reptile', 'snake', 'spider', 'wildlife', 'woman' ]

        # only submit jpegs and pngs 
        img_re = re.compile('\.(jpeg|jpg|png)$', re.IGNORECASE)
        for key in key_list:
            m = img_re.search(key)
            if m:
                image = {'S3Object': {'Bucket': bucket, 'Name': key}}
                logging.info('Submitting sample to Rekognition.detect_labels(%s)' % key)
                resp = rekog.detect_labels(Image=image, MinConfidence=70)

                # object detection bounding boxes are only sometimes available
                box = False
                detect_str = ''

                # Parse response, set tags if interesting labels found
                for x in resp['Labels']:
                    if x['Name'].lower() in life_labels:
                        detect_str = '%s %s' % (detect_str,x['Name'])
                        if not box:
                            try:
                                box = (x['Instances'][0]['BoundingBox'])
                            except Exception as e:
                                pass
                if box:
                    Tagging = { 'TagSet': [
                                { 'Key': 'life-labels', 'Value': detect_str, }, 
                                { 'Key': 'box-width', 'Value': str(box['Width']), }, 
                                { 'Key': 'box-height', 'Value': str(box['Height']), }, 
                                { 'Key': 'box-left', 'Value': str(box['Left']), }, 
                                { 'Key': 'box-top', 'Value': str(box['Top']), }, 
                                ] }
                elif detect_str:
                    Tagging = { 'TagSet': [ { 'Key': 'life-labels', 'Value': detect_str, }, ] }
                else:
                    detect_str = 'None'
                    Tagging = { 'TagSet': [ { 'Key': 'life-labels', 'Value': detect_str, }, ] }

                logging.info('Tagging object: %s tags: %s' % (key,detect_str))
                s3.put_object_tagging(Bucket=bucket, Key=key, Tagging=Tagging)

        return True


    @task()
    def Generate_bounding_box_images(status: str):
        """Add bounding box overlays in images with positive living object detections""" 

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        return True


    @task()
    def Build_static_site(status: str):
        """Build static site hosting images and life detections""" 

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        return True


    @task()
    def Notify_users(status: str):
        """Notify users when a new version of the site is published with new detections."""

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        return True

    img_list = NASA_API_get_mars_img_list()
    key_list = S3_put_images(img_list)
    status = Rekognition_detect_objects(key_list)
    status = Generate_bounding_box_images(status)
    status = Build_static_site(status)
    status = Notify_users(status)

mars_life_dag = mars_life_dag()
