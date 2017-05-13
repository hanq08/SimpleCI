
#!bin/bash

aws lambda create-function \
--region us-east-1 \
--function-name test-runner \
--zip-file fileb:///home/han/SimpleCI/test_repo/$1 \
--role arn:aws:iam::561819325006:role/lambda-basic-role \
--handler test_runner.my_handler \
--runtime python2.7 \
--profile adminuser