import boto3

ec2 = boto3.client('ec2')

vpcs = []
paginator = ec2.get_paginator('describe_vpcs')
pages = paginator.paginate()

for page in pages:
    for vpc in page['Vpcs']:
        vpcs.append(vpc)

for vpc in vpcs:
    print(f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}, Is Default: {vpc['IsDefault']}")