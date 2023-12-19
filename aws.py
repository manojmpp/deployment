import boto3
import base64

# Retrieve the secret value from AWS Secrets Manager
def get_secret():
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')
    response = client.get_secret_value(SecretId='my_secret_id')
    return response['SecretString']

# Retrieve the parameter value from AWS Systems Manager Parameter Store
def get_parameter():
    session = boto3.session.Session()
    client = session.client(service_name='ssm')
    response = client.get_parameter(Name='my_parameter_name', WithDecryption=True)
    return response['Parameter']['Value']

# Encode the secret using base64 encoding
def encode_secret(secret):
    return base64.b64encode(secret.encode())

# Decode the secret from base64 encoding
def decode_secret(encoded_secret):
    return base64.b64decode(encoded_secret).decode()