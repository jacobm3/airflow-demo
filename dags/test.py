import json
from datetime import datetime, timedelta

from airflow.decorators import dag, task # DAG and task decorators for interfacing with the TaskFlow API

# DAG-specific
import boto3
import json
import logging
import requests
from os.path import basename

from airflow.operators.python import get_current_context


@dag(
    dag_id='test_v06',
    # This defines how often your DAG will run, or the schedule by which your DAG runs. In this case, this DAG
    # will run every 30 mins
    schedule_interval=timedelta(days=1),
    # This DAG is set to run for the first time on January 1, 2021. Best practice is to use a static
    # start_date. Subsequent DAG runs are instantiated based on scheduler_interval
    start_date=datetime(2022, 5, 5),
    # When catchup=False, your DAG will only run for the latest schedule_interval. In this case, this means
    # that tasks will not be run between January 1, 2021 and 30 mins ago. When turned on, this DAG's first
    # run will be for the next 30 mins, per the schedule_interval
    catchup=True,
    max_active_runs=10,
    tags=['example']) # If set, this tag is shown in the DAG view of the Airflow UI

def test_dag():
    """
    ### Basic ETL Dag
    This is a simple ETL data pipeline example that demonstrates the use of
    the TaskFlow API using three simple tasks for extract, transform, and load.
    For more information on Airflow's TaskFlow API, reference documentation here:
    https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html
    """

    @task()
    def nasa_api_to_s3():
        '''
        #### Load 1 day of Mars images to s3
        A simple "extract" task that pulls Mars images from NASA API and loads them 
        into a timestamped s3 bucket directory for processing.
        '''

        context = get_current_context()
        date = context["logical_date"].strftime('%Y-%m-%d')

        bucket = 'jm3-airflow'
        nasa_api_key = 'HBc1WHi6sTtl7rtEHfJyGAWf7iCJ6t1VpyhPS50s'
        url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=%s&api_key=%s' % (date,nasa_api_key)
        max_imgs = 5

        response = requests.get(url)
        api_results = json.loads(response.text)

        s3 = boto3.client('s3')

        if len(api_results['photos']) == 0:

          # if no results for this date, upload no-results file
          logging.info('No results from api for %s' % date)
          key = 'img/%s/%s' % (date,'no-results.html')
          s3.put_object(Bucket=bucket, Key=key, ContentDisposition='inline', ContentType='text/html',
                        Body='Empty list from API.')
        else:
            # upload image results to s3
            for x in api_results['photos'][0:max_imgs]:
              imgurl = x['img_src']
              imgfname = basename(imgurl)
              key = 'img/%s/%s' % (date,imgfname)
              logging.info('Transferring %s' % imgurl)
              s3.put_object(Bucket=bucket, Key=key, ACL='public-read', ContentDisposition='inline', ContentType='image/jpeg',
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

    status = nasa_api_to_s3()

test_dag = test_dag()
