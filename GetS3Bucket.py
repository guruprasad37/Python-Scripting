import boto3
import requests

client = boto3.client('s3')

# Create a new S3 bucket with the specified name and region
#response = client.create_bucket(
#       Bucket='guruprasad337123',
#    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
#)

response = client.get_bucket_acl(
    Bucket='guruprasad337123'
)

res=response.json()

print(res["ResponseMetadata"]["RequestId"])