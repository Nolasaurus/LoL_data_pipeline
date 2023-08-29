#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Initialize counters for passed and failed tests
PASSED=0
FAILED=0

function run_test {
    python -m unittest $1
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}$1 PASSED${NC}"
        ((PASSED++))
    else
        echo -e "${RED}$1 FAILED${NC}"
        ((FAILED++))
    fi
}

# Iterate through test files in the 'tests' directory
for test_file in tests/test_*.py; do
    # Extract the module name from the file path
    test_module="tests.${test_file#tests/}"
    test_module="${test_module%.py}"
    
    # Run the test
    run_test $test_module
done

echo -e "\nAll tests completed."
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
