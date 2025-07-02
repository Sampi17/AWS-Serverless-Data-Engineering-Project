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

# 3. Build file name
file_name="yellow_tripdata_${year}-${month}.csv"

echo "➡️  Downloading $file_name..."

# 4. Download from Kaggle
# Download the specific file
kaggle datasets download -d elemento/nyc-yellow-taxi-trip-data \
  -f "$file_name" \
  -p data/
  
zip_file="data/${file_name}.zip" 

# Unzip csv file

unzip -o "$zip_file" 

if [ $? -ne 0 ]; then
  echo "❌ Download failed. File may not exist or Kaggle auth issue."
  exit 1
fi

# 5. Git commit and push to trigger CI/CD
git add "data/$file_name"
git commit -m "Add $file_name"
git push -u origin master

6. Increment month
next_month=$(date -d "$current_month-01 +1 month" +"%Y-%m")
echo "$next_month" > "$MARKER_FILE"

#echo "✅ Done. Next run will fetch $next_month"
