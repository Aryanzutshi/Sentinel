#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Usage: bash call_main.sh <parallel_processes> <choice (all, majority_all, majority_unique)>"
    exit 1
fi

parallel_processes=$1
choice=$2

echo "🔄 Running ScrawID analysis with $parallel_processes processes..."
python3 scripts/main.py $parallel_processes sample_results.txt $choice
