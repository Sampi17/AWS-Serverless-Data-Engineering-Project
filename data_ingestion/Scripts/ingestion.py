import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_nyc_2016_01(output_dir="data"):
    dataset_slug = "elemento/nyc-yellow-taxi-trip-data"
    target_file = "yellow_tripdata_2016-01.csv"

    # Create output dir if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    api = KaggleApi()
    api.authenticate()

    print(f"Downloading {target_file} from Kaggle dataset '{dataset_slug}'...")
    
    # Use download_file to get only the specific file
    api.dataset_download_file(dataset=dataset_slug,
                              file_name=target_file,
                              path=output_dir
                              )

    print(f"Downloaded and extracted to '{output_dir}'.")

if __name__ == "__main__":
    download_nyc_2016_01()
