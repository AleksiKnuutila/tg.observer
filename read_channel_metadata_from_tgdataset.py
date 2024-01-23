import json
import sys

def process_json(json_data):
    for key, value in list(json_data.items())[:100]:
        if 'text_messages' in value:
            del value['text_messages']
        if 'generic_media' in value:
            del value['generic_media']
        print(json.dumps({key: value}, indent=2))

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <json_filename>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path, 'r') as file:
        try:
            json_data = json.load(file)
            process_json(json_data)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

if __name__ == "__main__":
    main()
