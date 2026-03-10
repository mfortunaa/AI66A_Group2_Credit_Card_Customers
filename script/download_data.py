import os
import zipfile
import subprocess

# Define the target directory and Kaggle dataset name
DATA_DIR = os.path.join("data", "raw")
DATASET_NAME = "sakshigoyal7/credit-card-customers"

def download_and_extract():
    # Create the data/raw directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)
    print(f"[*] Checked/Created directory: {DATA_DIR}")

    # Use Kaggle CLI to download the dataset into DATA_DIR
    print(f"[*] Downloading dataset '{DATASET_NAME}' from Kaggle...")
    try:
        subprocess.run(["kaggle", "datasets", "download", "-d", DATASET_NAME, "-p", DATA_DIR], check=True)
        print("[+] Data downloaded successfully!")
    except subprocess.CalledProcessError:
        print("[-] Error: Could not download the dataset.")
        print("[-] Please ensure your Kaggle API token (kaggle.json) is properly configured in ~/.kaggle/")
        return

    # Extract the downloaded zip file
    zip_path = os.path.join(DATA_DIR, "credit-card-customers.zip")
    if os.path.exists(zip_path):
        print("[*] Extracting the zip file...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(DATA_DIR)
        print("[+] Extraction complete!")
        
        # Clean up by removing the zip file
        os.remove(zip_path)
        print("[*] Cleaned up the downloaded zip file.")
    else:
        print("[-] Warning: Zip file not found for extraction.")

if __name__ == "__main__":
    download_and_extract()