#!/bin/bash

echo "Running test_get_match_by_match_id..."
python -m unittest tests.test_get_match_by_match_id

echo "Running test_get_puuid_by_summon_id..."
python -m unittest tests.test_get_puuid_by_summon_id

echo "Running test_get_match_ids_by_puuid..."
python -m unittest tests.test_get_match_ids_by_puuid

# Add more test commands as needed

echo "All tests completed."
