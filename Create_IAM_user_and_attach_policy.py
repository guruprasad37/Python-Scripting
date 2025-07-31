import boto3

iam=boto3.client("iam")

iam.create_user(UserName='Test12345')

iam.attach_user_policy(
    UserName='Test12345',
    PolicyArn='arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess'
)
