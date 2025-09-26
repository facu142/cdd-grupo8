import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("yashdevladdha/uber-ride-analytics-dashboard")
print("Path to dataset files:", path)

# List files in the downloaded folder
files = os.listdir(path)
print("Files in the dataset:", files)

# Read a CSV file (for example, the first one)
csv_file = [f for f in files if f.endswith('.csv')][0]
df = pd.read_csv(os.path.join(path, csv_file))
print(df.head())

