#!/usr/bin/env python

import boto3
import sys
import os

BUCKET = 'your_bucket_name'

s3r = boto3.resource('s3')
bucket = s3r.Bucket(BUCKET)

c = len(sys.argv)
if c == 2 and os.path.isfile(sys.argv[1]):
  # list all objects in bucket.
  KEYS = [obj.key for obj in bucket.objects.all()]
  for key in KEYS:
      if key == sys.argv[1] :
        print(sys.argv[1] + " already exist.")
        sys.exit(2)
  # upload
  bucket.upload_file(sys.argv[1], sys.argv[1])
else:
  print(sys.argv[1] + " not found.")

