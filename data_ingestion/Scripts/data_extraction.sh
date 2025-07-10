#!/bin/bash

current_dir=$(pwd)

# downloading the dataset from kaggle using an api 
python "$current_dir/Script/ingestion.py"

#unzip file
echo "unziping zip dataset"
unzip -O "$current_dir/dataset/yellow_tripdata_2016-01.csv" -d data/

# partitions the data for easy uploads
python "$current_dir/Script/partition.py"

# upload to S3 bucket
python "$current_dir/Script/upload_to_s3.py"


