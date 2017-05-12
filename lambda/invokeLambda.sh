
#!bin/bash

aws lambda invoke \
--invocation-type RequestResponse \
--function-name test-runner \
--region us-east-1 \
--log-type Tail \
--payload '{"key1":"value1", "key2":"value2", "key3":"value3"}' \
--profile adminuser \
outputfile.txt 