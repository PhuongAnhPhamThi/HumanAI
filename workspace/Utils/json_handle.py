import json
import os


def extract_json_from_string(string_with_json):
    start_index = string_with_json.find('{')
    end_index = string_with_json.rfind('}') + 1

    # Extract the JSON string
    json_string = string_with_json[start_index:end_index]
    # Load JSON string into dictionary
    extracted_json = json.loads(json_string)

    return extracted_json


def write_to_json_file(jsonfile: str, jsonvalue, key: str = None):
    file_path = os.path.join("workspace") + "/"
    with open(file_path + jsonfile, "r", encoding="utf-8") as f:
        existing_data = json.load(f)
    if key is not None:
        if key in existing_data:
            existing_data[key].update(jsonvalue)
        else:
            existing_data[key] = {}
            existing_data[key].update(jsonvalue)
    else:
        existing_data.update(jsonvalue)
    # Write JSON data to file
    with open(file_path + "ebookInfo.json", 'w', encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)


def remove_values_json():
    file_path = os.path.join("workspace") + "/"
    with open(file_path + "ebookInfo.json", "r", encoding="utf-8") as f:
        existing_data = json.load(f)
    if isinstance(existing_data, dict):
        for key in existing_data:
            if isinstance(existing_data[key], dict) or key == "kapiteln" or key == "metadaten":
                existing_data[key] = {}  # Set value to None
            elif isinstance(existing_data[key], str):
                existing_data[key] = ""
    with open(file_path + "ebookInfo.json", 'w', encoding="utf-8") as file:
        json.dump(existing_data, file, indent=4, ensure_ascii=False)

