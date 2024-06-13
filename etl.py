import os
import json
import pandas as pd

# Print the current working directory
print("Current Working Directory:", os.getcwd())

# Load the JSON data
try:
    with open('orchestra_data.json') as f:
        data = json.load(f)
except FileNotFoundError as e:
    print("File not found. Please check the file path and try again.")
    raise e

# Normalize and flatten the JSON
concerts = pd.json_normalize(data, 'concerts', ['orchestra', 'season', 'location'], errors='ignore', record_prefix='concert_')
works = pd.json_normalize(data, ['concerts', 'works'], ['title', 'composer'], errors='ignore', record_prefix='work_')
artists = pd.json_normalize(data, ['concerts', 'works', 'soloists'], ['name', 'instrument'], errors='ignore', record_prefix='artist_')

# Save the normalized data to CSV
concerts.to_csv('data/concerts.csv', index=False)
works.to_csv('data/works.csv', index=False)
artists.to_csv('data/artists.csv', index=False)
