#!/bin/bash

# pytest==8.4.1 and pytest-json-ctrf==0.3.5 are baked into the environment image (environment/Dockerfile).

mkdir -p /logs/verifier

# This runs pytest
pytest --ctrf /logs/verifier/ctrf.json /tests/test_outputs.py


# This writes reward.txt


if [ $pytest_exit_code -eq 0 ]; then
  echo "1" > /logs/verifier/reward.txt
else
  echo "0" > /logs/verifier/reward.txt
fi
exit $pytest_exit_code
