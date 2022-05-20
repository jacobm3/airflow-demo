import json
from datetime import datetime, timedelta

from airflow.decorators import dag, task # DAG and task decorators for interfacing with the TaskFlow API

import boto3
import json
import logging
import requests
from os.path import basename

from airflow.operators.python import get_current_context

bucket = 'jm3-airflow'

@dag(
    dag_id='mars_life_v05',
    # This defines how often your DAG will run, or the schedule by which your DAG runs. In this case, this DAG
    # will run every 30 mins
    schedule_interval=timedelta(days=1),
    # This DAG is set to run for the first time on January 1, 2021. Best practice is to use a static
    # start_date. Subsequent DAG runs are instantiated based on scheduler_interval
    start_date=datetime(2022, 5, 1),
    # When catchup=False, your DAG will only run for the latest schedule_interval. In this case, this means
    # that tasks will not be run between January 1, 2021 and 30 mins ago. When turned on, this DAG's first
    # run will be for the next 30 mins, per the schedule_interval
    catchup=True,
    max_active_runs=5,
    tags=['example']) # If set, this tag is shown in the DAG view of the Airflow UI


def mars_life_dag():
    """
    ### ETL Dag
    """

    @task()
    def NASA_API_get_mars_img_list():
        '''
        #### Load 1 day of Mars images to s3
        Extract - pulls Mars images from NASA API for the current date
        '''

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        nasa_api_key = 'HBc1WHi6sTtl7rtEHfJyGAWf7iCJ6t1VpyhPS50s'
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=%s&api_key=%s' % (date,nasa_api_key)
        max_imgs = 5

        response = requests.get(url)
        api_results = json.loads(response.text)

        img_list = []
        for x in api_results['photos'][0:max_imgs]:
            img_list.append(x['img_src'])

        return img_list


    @task()
    def S3_put_imgs(img_list: list):

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        s3 = boto3.client('s3')

        if len(img_list) == 0:
            logging.info('No results from api for %s' % date)
            key = 'img/%s/%s' % (date,'no-results.html')
            s3.put_object(Bucket=bucket, Key=key, Body='Empty list from API on %s.' % date)
        else:
            for imgurl in img_list:
                imgfname = basename(imgurl)
                key = 'img/%s/%s' % (date,imgfname)
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
                dest.copy(source, 'img/%s/%s' % (date,sample))

        return True

    img_list = NASA_API_get_mars_img_list()
    status = S3_put_imgs(img_list)

mars_life_dag = mars_life_dag()
