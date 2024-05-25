import os
import json
import subprocess
from jinja2 import Template
import requests

def download_image(image_url, output_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        print("Image downloaded successfully.")
    else:
        print("Failed to download the image.")

def escape_latex(s):
    # Function to escape LaTeX special characters
    return s.replace('&', r'\&').replace('%', r'\%').replace('$', r'\$').replace('#', r'\#').replace('_',
                                                                                                     r'\_').replace(
        '{', r'\{').replace('}', r'\}').replace('~', r'\textasciitilde{}').replace('^', r'\^{}').replace('\\',
                                                                                                         r'')

def generate_pdf():
    def compile_latex(tex_file, output_dir):
        subprocess.run(['pdflatex', '-output-directory=' + output_dir, tex_file], cwd=file_path_latex)

    # File paths
    file_path_latex = "workspace/Ebook_Latex/"
    output_dir = "C:/Users/admin/PycharmProjects/HumanAI/workspace/Ebook_Latex/out"

    # Load JSON data
    with open('workspace/ebookInfo.json') as f:
        data = json.load(f)

    # Escape special characters in JSON data
    data = {k: escape_latex(v) if isinstance(v, str) else v for k, v in data.items()}
    data['kapiteln'] = {k: {sub_k: escape_latex(sub_v) if isinstance(sub_v, str) else sub_v for sub_k, sub_v in sub_v.items()} for k, sub_v in data['kapiteln'].items()}

    # Download cover image
    download_image(data['cover_link'], os.path.join(file_path_latex, "cover.jpg"))

    # Load LaTeX template
    with open(os.path.join(file_path_latex, 'template.tex')) as f:
        template_str = f.read()

    # Create Jinja2 Template object
    template = Template(template_str)

    # Add cover image path to data
    data['cover'] = 'cover.jpg'

    # Render LaTeX template with data
    latex_content = template.render(data=data)

    # Write rendered LaTeX content to file
    with open(os.path.join(file_path_latex, 'output.tex'), 'w') as f:
        f.write(latex_content)

    # Compile LaTeX file with specified output directory
    compile_latex('output.tex', output_dir)

if __name__ == "__main__":
    generate_pdf()
