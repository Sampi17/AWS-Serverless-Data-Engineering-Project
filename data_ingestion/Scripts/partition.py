import os
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

def partition_and_convert_to_parquet(
    csv_file="data/yellow_tripdata_2016-01.csv",
    output_dir="data/partitioned_parquet"
):
    print("Loading CSV...")
    df = pd.read_csv(csv_file, parse_dates=['tpep_pickup_datetime'])
    
    # Add partition columns
    df['year'] = df['tpep_pickup_datetime'].dt.year
    df['month'] = df['tpep_pickup_datetime'].dt.month
    df['day'] = df['tpep_pickup_datetime'].dt.day
    
    print(f"DataFrame shape: {df.shape}")
    print("Converting & partitioning...")
    
    # Create output dir
    os.makedirs(output_dir, exist_ok=True)
    
    # Group by day and save each as partitioned Parquet
    for (year, month, day), group in df.groupby(['year', 'month', 'day']):
        partition_path = os.path.join(
            output_dir,
            f"year={year}/month={str(month).zfill(2)}/day={str(day).zfill(2)}"
        )
        os.makedirs(partition_path, exist_ok=True)
        
        file_path = os.path.join(partition_path, "part-000.parquet")
        
        # Convert group DataFrame to PyArrow Table
        table = pa.Table.from_pandas(group)
        
        # Write as Parquet
        pq.write_table(table, file_path)
        
        print(f"Written: {file_path} [{group.shape[0]} rows]")
    
    print("✅ All done! Partitioned Parquet files are ready.")

if __name__ == "__main__":
    partition_and_convert_to_parquet()
