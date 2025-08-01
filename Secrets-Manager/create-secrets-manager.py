import boto3

client = boto3.client('secretsmanager', region_name='us-east-1')

response = client.create_secret(
    Name='MyApp_DB_Credentials',  
    Description='Database credentials for MyApp',
    SecretString='{"username":"admin","password":"MySecureP@ssw0rd"}'
)

print("Secret created:", response['ARN'])
