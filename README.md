# SimpleCI
This is a simplified continuous integration system. This project modify [SuperSimpleCI](https://github.com/aosabook/500lines/tree/master/ci) to a serverless system built with Amazon Lambda. 

## Files
* repo_observer.py -- Checks the repo for changes and notifies the dispatcher
* dispatcher.py -- Receives test requests and call a aws lambda function test runners
* test_runner.py -- A amazon lambda function which runs the tests and returns the results 
* helpers.py -- Holds shared code
* update_repo.sh -- Updates the shared repo and drops a new file with the commit id if there's a change
* run_or_fail.sh -- Helper method used in update_repo.sh and test_runner_script.sh
* tests/ -- Holds some demo tests to run

## Quick Start
### 1. Setup Amazon Lambda Function
### 2. File Setup
### 3. Run the CI system
