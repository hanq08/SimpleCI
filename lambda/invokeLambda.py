import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)

client = boto3.client('lambda')
logger = boto3.client('logs')



response = client.invoke(
    FunctionName='test-runner',
    InvocationType='Event',
    LogType='Tail',
    ClientContext='string',
    Payload=b'{"message":"message"}'
)





pp.pprint(response)


