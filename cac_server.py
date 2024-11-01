import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# File path for storing scan results
RESULTS_FILE = "cac_results.json"

# Initialize an empty list to store scan results in memory
scan_results = []

# Function to write scan results to the file
def save_results_to_file(data):
    with open(RESULTS_FILE, 'a') as f:
        f.write(json.dumps(data) + '\n')  # Write each result as a JSON line

# Define a custom handler class to handle POST requests
class ScanRequestHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        # Determine the length of the incoming data
        content_length = int(self.headers['Content-Length'])
        # Read and decode the incoming JSON data
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Try to parse the JSON data and add it to scan_results
        try:
            data = json.loads(post_data)
            if 'ip' in data and 'status' in data:
                scan_results.append(data)
                save_results_to_file(data)  # Save to file
                print(f"Received scan result: {data}")
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"Data received and added to the list and file.")
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid data format.")
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON.")

    def do_GET(self):
        # Handle GET requests to view current scan results
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(scan_results).encode('utf-8'))

# Run the server on port 8080
def run(server_class=HTTPServer, handler_class=ScanRequestHandler, port=4420):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

# Start the server
run()
