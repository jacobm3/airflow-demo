#!/usr/bin/python3

import base64
import boto3
import json
import sys

rekog = boto3.client('rekognition')

bucket = 'jm3-airflow'
key = 'img/2022-05-01/FLB_705202199EDR_F0943386FHAZ00200M_pos1.JPG'


# Detect life-like objects
life_labels = [ 'animal', 'arachnid', 'face', 'female', 'horse', 'human',
    'insect', 'invertebrate', 'male', 'mammal', 'man', 'people', 'person',
    'reptile', 'snake', 'spider', 'wildlife', 'woman' ]

image = {'S3Object': {'Bucket': bucket, 'Name': key}}
resp = rekog.detect_labels(Image=image, MinConfidence=70)

s3 = boto3.client('s3')

#print(json.dumps(resp))

detect_str = ''
box = ''
Tagging = { 'TagSet': [ { 'Key': 'life-labels', 'Value': 'None', }, ] }

# Parse response, set tags if interesting labels found
for x in resp['Labels']:
    if x['Name'].lower() in life_labels:
        detect_str = '%s %s' % (detect_str,x['Name'])
        try:
            box = (x['Instances'][0]['BoundingBox'])
        except Exception as e:
            pass
        Tagging = { 'TagSet': [
                    { 'Key': 'life-labels', 'Value': detect_str, }, 
                    { 'Key': 'box-width', 'Value': str(box['Width']), }, 
                    { 'Key': 'box-height', 'Value': str(box['Height']), }, 
                    { 'Key': 'box-left', 'Value': str(box['Left']), }, 
                    { 'Key': 'box-top', 'Value': str(box['Top']), }, 
                    ] }

# Tag the image in s3
s3.put_object_tagging(Bucket=bucket, Key=key, Tagging=Tagging)


