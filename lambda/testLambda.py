import boto3
import pprint

pp = pprint.PrettyPrinter(indent=2)
client = boto3.client('lambda')
pp.pprint(client.list_functions())