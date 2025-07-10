import os
import boto3

# Config
BUCKET_NAME = "my-data-lake-17"
LOCAL_PARQUET_DIR = "data/partitioned_parquet/"
S3_PREFIX = "data/raw/partitioned_parquet/"  # put partitioned parquet inside data/raw/

# Init S3 client (uses credentials from ~/.aws/credentials or env vars)
s3 = boto3.client("s3")

def upload_parquet_files():
    for root, dirs, files in os.walk(LOCAL_PARQUET_DIR):
        for filename in files:
            if filename.endswith(".parquet"):
                local_path = os.path.join(root, filename)
                
                # keep partition folders relative to LOCAL_PARQUET_DIR
                relative_path = os.path.relpath(local_path, LOCAL_PARQUET_DIR)
                
                # build final S3 key
                s3_key = os.path.join(S3_PREFIX, relative_path).replace("\\", "/")
                
                print(f"Uploading {local_path} to s3://{BUCKET_NAME}/{s3_key}")
                s3.upload_file(local_path, BUCKET_NAME, s3_key)
                print(f"✅ Uploaded {s3_key}")

if __name__ == "__main__":
    upload_parquet_files()
