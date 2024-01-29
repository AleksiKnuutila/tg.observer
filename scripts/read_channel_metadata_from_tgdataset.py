import json
import os
import pandas as pd
import sys

def process_json(json_data):
    for channel_id, channel_data in json_data.items():
        if 'text_messages' in channel_data:
            del channel_data['text_messages']
        if 'generic_media' in channel_data:
            del channel_data['generic_media']
    return json_data

def process_directory(directory_path):
    concatenated_results = []

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)

            print(f"Processing file: {file_path}")

            with open(file_path, 'r') as file:
                try:
                    json_data = json.load(file)
                    processed_data = process_json(json_data)
                    concatenated_results.append(processed_data)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {file_path}: {e}")

    return concatenated_results

def write_to_csv(data, output_path='output.csv'):
    if data:
        # Concatenate the list of dictionaries into a single dictionary
        concatenated_data = {}
        for item in data:
            concatenated_data.update(item)

        df = pd.DataFrame(list(concatenated_data.values()), index=list(concatenated_data.keys()))
        df.to_csv(output_path, index_label='ID')

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    if not os.path.isdir(directory_path):
        print("Error: The specified path is not a directory.")
        sys.exit(1)

    results = process_directory(directory_path)

    # Write data to CSV using pandas
    write_to_csv(results)

if __name__ == "__main__":
    main()
