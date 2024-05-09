
import http.server
import socketserver
import webbrowser
import os

def start_server(port=8000, html_file_path="workspace/output.html"):
    # Check if the HTML file exists
    if not os.path.isfile(html_file_path):
        print(f"Error: HTML file '{html_file_path}' not found.")
        return

    # Create a custom handler to serve the HTML file
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=os.path.dirname(html_file_path), **kwargs)

        # Override the do_GET method to serve the HTML file for the root URL
        def do_GET(self):
            if self.path == "/":
                self.path = os.path.basename(html_file_path)
            return super().do_GET()

    # Create a TCP server with SO_REUSEADDR option
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        httpd.allow_reuse_address = True  # Set the SO_REUSEADDR option
        print(f"Server started at http://localhost:{port}")
        # Open the web browser to view the HTML content
        webbrowser.open_new_tab(f"http://localhost:{port}")
        # Serve requests indefinitely
        httpd.serve_forever()