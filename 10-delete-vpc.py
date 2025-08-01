import boto3

# Initialize the EC2 client
ec2_client = boto3.client('ec2')
paginator = ec2_client.get_paginator('describe_vpcs')
# Specify the VPC ID to delete
vpc_id_to_delete = 'vpc-03ad1c660621a8661' # Replace with your VPC ID

try:
    # Attempt to delete the VPC
    response = ec2_client.delete_vpc(
        VpcId=vpc_id_to_delete
    )
    print(f"VPC {vpc_id_to_delete} deleted successfully.")
except ec2_client.exceptions.ClientError as e:
    print(f"Error deleting VPC {vpc_id_to_delete}: {e}")
