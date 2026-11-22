#!/bin/bash
cd "$(dirname "$0")"
python run_cases.py p3zero 14 > run_p3zero_n14.log 2>&1
python run_cases.py p2d3chi1 12 > run_p2d3chi1_n12.log 2>&1
python run_cases.py p2d1h 12 > run_p2d1h_n12.log 2>&1
python run_cases.py p2d2irrdeep 13 > run_p2d2irrdeep_n13.log 2>&1
echo CHAIN-DONE > chain_done.txt
