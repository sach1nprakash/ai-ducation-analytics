import json
import os
import requests

# Define the path to the NDJSON file
ndjson_file_path = 'dataset/label-box/mid-bored-wiki.ndjson'  # Change this to the path of your NDJSON file

# Define the directory where you want to save the images
save_directory = 'imagesbored'  # Change this to your desired directory

# Ensure the directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Read the NDJSON file line by line and process each JSON object
with open(ndjson_file_path, 'r') as ndjson_file:
    for index, line in enumerate(ndjson_file, start=1):
        try:
            data = json.loads(line)

            # Get the image URL from the JSON data
            image_url = data['data_row']['row_data']

            # Extract the image filename from the URL
            image_filename = os.path.join(
                save_directory, f'mid_bored_{index:04d}.png'
            )

            # Download and save the image as .png
            response = requests.get(image_url)
            if response.status_code == 200:
                with open(image_filename, 'wb') as f:
                    f.write(response.content)
                print(f"Image saved as {image_filename}")
            else:
                print(f"Failed to download the image from {image_url}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except KeyError as e:
            print(f"KeyError: {e}")