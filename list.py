#!/usr/bin/env python

import boto3

BUCKET = 'your_bucket_name'

s3r = boto3.resource('s3')
bucket = s3r.Bucket(BUCKET)

# list all objects in bucket.
KEYS = [obj.key for obj in bucket.objects.all()]
for key in KEYS:
    print(key)
