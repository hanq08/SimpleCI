import boto3
import pprint
import subprocess
import base64

def invoke():

	subprocess.check_output("/home/han/SimpleCI/testrunner/deployTest.sh", shell=True)

	pp = pprint.PrettyPrinter(indent=2)

	client = boto3.client('lambda')

	response = client.invoke(
	FunctionName='test-runner',
	InvocationType='RequestResponse',
	LogType='Tail',
	)

	print base64.b64decode(response['LogResult']) 

if __name__ == "__main__":
    invoke()

