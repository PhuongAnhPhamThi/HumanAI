import os
import json
from jinja2 import Template

file_path = os.path.join("workspace") + "/"


def update_html_from_json():
    # Hardcoded filenames
    json_file = file_path + 'ebookInfo.json'
    html_file = file_path + 'baseline.html'
    output_file = file_path + 'output.html'

    # Read JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Read HTML content from the specified file
    with open(html_file, 'r') as f:
        template = Template(f.read())

    # Render the template with JSON data
    updated_html_content = template.render(data=data)

    # Write the updated HTML content back to the file
    with open(output_file, 'w') as f:
        f.write(updated_html_content)

