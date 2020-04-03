#!/usr/bin/env python

import boto3
import sys
import os

BUCKET = 'your_bucket_name'

s3r = boto3.resource('s3')
bucket = s3r.Bucket(BUCKET)

c = len(sys.argv)
if c == 3 :
  KEYS = [obj.key for obj in bucket.objects.all()]
  for key in KEYS:
    if key == sys.argv[1]:
      if os.path.isfile(sys.argv[2]) :
        # download file already exist.
        print(sys.argv[2] + " already exist.")
      else:
        # download
        bucket.download_file(sys.argv[1], sys.argv[2])
      sys.exit(0)
  print(sys.argv[1] + " not found on this bucket.")
else:
  print("usage: donwload.py <object on bucket> <donwload object>")

