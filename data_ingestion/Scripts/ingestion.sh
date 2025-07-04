#!/bin/bash

# File: simulated_monthly_download.sh

# Project root
cd ~/aws_projects/aws_data_engineering_p1/data_ingestion

# Create data folder if not exists
mkdir -p data

# 1. Read current month marker
MARKER_FILE="data/.current_month"

# If marker doesn't exist, start at Jan 2016
if [ ! -f "$MARKER_FILE" ]; then
  echo "2016-01" > "$MARKER_FILE"
fi

# 2. Read current marker (YYYY-MM)
current_month=$(cat "$MARKER_FILE")
year=$(echo "$current_month" | cut -d '-' -f 1)
month=$(echo "$current_month" | cut -d '-' -f 2)

# File name to request from Kaggle
file_name="yellow_tripdata_${year}-${month}.csv"

echo "➡️  Downloading $file_name as ZIP..."

# Download as zip into data/
kaggle datasets download -d elemento/nyc-yellow-taxi-trip-data \
  -f "$file_name" \
  -p dataset/ 
downloaded_file="dataset/$file_name"

unzip $downloaded_file -d data/

git add $MARKER_FILE
echo "adding $MARKER_FILE to git staging area"
git commit -m "downloaded dataset and triggering CI/CD to move the csv file to s3 bucket"
echo "committed changes"
git push -u origin master 