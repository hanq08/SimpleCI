import boto3

client = boto3.client('lambda')
print client.get_function("test_runner")
