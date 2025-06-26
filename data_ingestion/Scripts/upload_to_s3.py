import os
import boto3

# Configuration
BUCKET_NAME = "my-data-lake-17 " 
DATA_DIR = "data"
S3_PREFIX = "raw/"  # prefix in S3 bucket

# Initialize S3 client (uses credentials from env vars)
s3 = boto3.client("s3")

def upload_csv_files():
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".csv"):
            local_path = os.path.join(DATA_DIR, filename)
            s3_key = os.path.join(S3_PREFIX, filename)
            print(f"Uploading {filename} to s3://{BUCKET_NAME}/{s3_key}")
            s3.upload_file(local_path, BUCKET_NAME, s3_key)
            print(f"✅ Uploaded {filename}")

if __name__ == "__main__":
    upload_csv_files()
