# SimpleCI
This is a simplified continuous integration system. This project modifies [SuperSimpleCI](https://github.com/aosabook/500lines/tree/master/ci) to a serverless system built with Amazon Lambda. 

## Files
* repo_observer.py -- Checks the repo for changes and notifies the dispatcher
* dispatcher.py -- Receives test requests and call aws lambda function test runners
* test_runner.py -- A amazon lambda function which runs the tests and returns the results 
* helpers.py -- Holds shared code
* update_repo.sh -- Updates the shared repo and drops a new file with the commit id if there's a change
* run_or_fail.sh -- Helper method used in update_repo.sh and test_runner_script.sh
* test_repository/ -- This will be our master repository. This is where developers check in their code, and repo_observer.py check for commits, and inform dispatcher to call lambda tests.

## Quick Start
### 1. Setup Amazon Lambda Function
### 2. Setup
### 3. Run the CI system
