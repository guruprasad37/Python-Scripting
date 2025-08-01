import boto3
from datetime import datetime

ec2 = boto3.client('ec2')  # Connect to EC2 service

def create_snapsho (volume_id, description):
    response = ec2.create_snapshot(
        VolumeId=volume_id,  # EBS volume ID
        Description=description,  # Snapshot description
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [{'Key': 'CreatedBy', 'Value': 'PythonScript'}]
            }
        ]
    )
    print(f"Snapshot created: {response['SnapshotId']}")
