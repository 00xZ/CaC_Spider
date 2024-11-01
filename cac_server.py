from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Configuration for the server
HOST = '127.0.0.1'  # Change to '' to allow all interfaces
PORT = 4420
AUTH_KEY = "your_secret_key"  # Replace with your actual secret key
OUTPUT_FILE = "cac_results.json"

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Read content length
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        
        # Check for the key in the request
        key = self.headers.get('Authorization')
        
        if key == AUTH_KEY:
            # Process the valid request
            try:
                # Parse the received data
                data = json.loads(post_data)

                # Write to the output file
                with open(OUTPUT_FILE, 'a') as f:
                    f.write(json.dumps(data) + "\n")

                # Respond with success
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Successfully written to file.')
            except json.JSONDecodeError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Invalid JSON format.')
        else:
            # Reject request if the key is invalid
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b'Forbidden: Invalid Key.')

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = (HOST, PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on http://{HOST}:{PORT}/')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
