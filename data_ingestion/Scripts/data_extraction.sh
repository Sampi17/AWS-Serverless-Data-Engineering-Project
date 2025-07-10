#!/bin/bash

current_dir="$(pwd)/Scripts

#  
python "$current_dir/ingestion.py"

python "$current_dir/partition.py"

python "$current_dir/upload_to_s3.py"


