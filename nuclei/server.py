from flask import Flask, render_template, jsonify#flask server to show CVE scan on a web server
import json

app = Flask(__name__)

# Load the cleaned CVE data (JSON file)
with open('vuln_cleaned_with_severity.json') as f:
    cve_data = json.load(f)

@app.route('/')
def index():
    # Pass the CVE data to the template
    return render_template('index.html', cve_data=cve_data)

@app.route('/api/cve-data')
def api_cve_data():
    # Serve CVE data as JSON for potential AJAX requests
    return jsonify(cve_data)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)  # Change port to 8000 (or any other desired port)
