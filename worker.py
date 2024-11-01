import requests
import json

# Define the server URL
server_url = 'http://127.0.0.1:4420'  # Replace with your server's IP

# Client authorization key (must match the server's key)
AUTH_KEY = "your_secret_key"  # Replace with the actual key

# File containing scan data
DATA_FILE = "db.json"

# Function to send scan data to the server
def send_scan_data(scan_data):
    try:
        # Set up headers with the authorization key
        headers = {
            'Authorization': AUTH_KEY,
            'Content-Type': 'application/json'
        }
        
        # Send the POST request with the JSON data and headers
        response = requests.post(server_url, json=scan_data, headers=headers)
        
        # Print the server's response
        print(response.text)
    except requests.RequestException as e:
        print("Error sending data:", e)

# Read data from db.json and send as a list to the server
try:
    with open(DATA_FILE, 'r') as file:
        # Read entire file content and parse as JSON array
        content = file.read()
        try:
            scan_data_list = json.loads(content)  # This should be a list of JSON objects
            
            # Send the entire list of scan data to the server if it's not empty
            if scan_data_list:
                send_scan_data(scan_data_list)
        except json.JSONDecodeError:
            print("Invalid JSON format in file.")
except FileNotFoundError:
    print(f"File '{DATA_FILE}' not found.")
