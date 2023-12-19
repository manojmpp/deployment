import boto3

def get_secret():
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager')
    response = client.get_secret_value(SecretId='my_secret_id')
    return response['SecretString']

# Get the secret value and print it
secret_value = get_secret()
print(f"Secret value: {secret_value}")