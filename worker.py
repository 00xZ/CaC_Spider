import requests
import json

# Define the server URL
server_url = 'http://127.0.0.1:4420'  # Replace with your server's IP
AUTH_KEY = "your_secret_key"  
# File containing scan data
DATA_FILE = "db.json"

# Function to send scan data to the server
def send_scan_data(scan_data):
    try:
        headers = {
            'Authorization': AUTH_KEY,
            'Content-Type': 'application/json'
        }
        response = requests.post(server_url, json=scan_data, headers=headers)
        print(response.text)
    except requests.RequestException as e:
        print("Error sending data:", e)

# Read data from spidered.txt and send each line to the server
try:
    with open(DATA_FILE, 'r') as file:
        for line in file:
            try:
                # Parse each line as a JSON object
                scan_data = json.loads(line.strip())
                # Send the JSON data to the server
                send_scan_data(scan_data)
            except json.JSONDecodeError:
                print("Invalid JSON format in line:", line)
except FileNotFoundError:
    print(f"File '{DATA_FILE}' not found.")
