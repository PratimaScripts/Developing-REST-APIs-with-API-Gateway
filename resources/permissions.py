'''
	You must replace <bucket-name> with your actual bucket name
'''
import boto3
import json

S3API = boto3.client("s3", region_name="us-east-1")
bucket_name = "c85205a1816270l4418703t1w946914026251-s3bucket-sc2ktcvzen8p"

policy_file = open("/home/ec2-user/environment/resources/website_security_policy.json", "r")


S3API.put_bucket_policy(
    Bucket = bucket_name,
    Policy = policy_file.read()
)
print ("DONE")
