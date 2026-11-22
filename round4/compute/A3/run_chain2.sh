#!/bin/bash
cd "$(dirname "$0")"
while [ ! -f chain_done.txt ]; do sleep 15; done
python run_cases.py p2d1K6 12 > run_p2d1K6_n12.log 2>&1
echo CHAIN2-DONE > chain2_done.txt
