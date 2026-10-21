#!/usr/bin/env bash
# Feeds the monthly customer extracts to your snapshot one at a time, oldest first.
#
# A dbt snapshot records changes between runs. Our CRM only gives us one full copy of the customer
# table per month (customer_extracts.csv, column extract_date). This script runs
#     dbt snapshot --vars "{extract_date: 'YYYY-MM-DD'}"
# once per extract, in date order. Your snapshot must read ONLY the extract named by var('extract_date').
#
# Usage:  ./scripts/replay_customer_extracts.sh            (from the project folder)
set -euo pipefail
cd "$(dirname "$0")/.."
RAW_DIR="${HT_RAW_DIR:-data/raw}"
DATES=$(python3 -c "
import csv
print(' '.join(sorted({r['extract_date'] for r in csv.DictReader(open('$RAW_DIR/customer_extracts.csv'))})))")
for d in $DATES; do
  echo "== dbt snapshot for extract $d"
  dbt snapshot --vars "{extract_date: '$d'}"
done
