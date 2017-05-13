
#!bin/bash

cd /home/han/SimpleCI/test_repo
zip -FSr test_repo.zip *
cd ../lambda
./updateLambda.sh test_repo.zip