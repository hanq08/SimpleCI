
#!bin/bash

cd /home/han/SimpleCI/test_repo
zip -FSr test_repo.zip *
cd ../testrunner
./updateTest.sh test_repo.zip
exit 0