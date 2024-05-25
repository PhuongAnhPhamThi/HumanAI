import json
import os
from workspace.Utils.text_handle import write_to_txt_file_simple, read_from_txt_file


def extract_json_from_string_inhalt(string_with_json):
    write_to_txt_file_simple(txt="json.txt", actiontype="w", text=string_with_json)
    string_with_json1 = read_from_txt_file(txt="json.txt", actiontype="r")
    start_index = string_with_json1.find('{')
    end_index = string_with_json1.rfind('}') + 1

    json_string = string_with_json1[start_index:end_index]

    inhalt_str = json_string[json_string.index("Kapitel Inhalt Teil")+25:json_string.rfind('"')]
    #escaped_str = inhalt_str.replace('\"', "'").replace('"', "'").replace('\\', '').replace('\n', '').replace('\t','').replace("\'", '').replace("/", '')
    escaped_str = inhalt_str.replace('\"', "'").replace('\\', '').replace('\t', '').replace('"', "'")
    full_str = json_string[:json_string.index("Kapitel Inhalt Teil")+25] + escaped_str + json_string[json_string.rfind('"'):]
    print("full_str")
    print(full_str)
    extracted_json = json.loads(full_str, strict=False)

    return extracted_json

def extract_json_from_string(string_with_json):
    start_index = string_with_json.find('{')
    end_index = string_with_json.rfind('}') + 1

    # Extract the JSON string
    json_string = string_with_json[start_index:end_index]
    # Load JSON string into dictionary
    extracted_json = json.loads(json_string,strict=False)

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
