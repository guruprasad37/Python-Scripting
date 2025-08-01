import boto3

ec2 = boto3.resource('ec2')
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{"Key": "Name", "Value": "my-boto3-vpc"}])
vpc.wait_until_available()
print(f"VPC created with ID: {vpc.id}")


