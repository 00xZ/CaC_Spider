import json

# Input JSON file
input_file = "corrected_cac_results.json"
# Output HTML file
output_file = "cac_results.html"

def convert_json_to_html(input_file, output_file):
    try:
        # Read the JSON file
        with open(input_file, 'r') as file:
            data = json.load(file)  # Load the JSON data

        # Start the HTML content
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>CAC Results</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 20px; }
                table { border-collapse: collapse; width: 100%; margin-top: 20px; }
                th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
                th { background-color: #f4f4f4; }
                tr:nth-child(even) { background-color: #f9f9f9; }
            </style>
        </head>
        <body>
            <h1>CAC Results</h1>
            <table>
                <tr>
                    <th>URL</th>
                    <th>Status Code</th>
                    <th>Description</th>
                </tr>
        """

        # Add rows to the table for each JSON object
        for entry in data:
            url = entry.get("url", "N/A")
            status_code = entry.get("status_code", "N/A")
            description = entry.get("description", "N/A")
            html_content += f"""
                <tr>
                    <td><a href="{url}" target="_blank">{url}</a></td>
                    <td>{status_code}</td>
                    <td>{description}</td>
                </tr>
            """

        # Close the table and HTML
        html_content += """
            </table>
        </body>
        </html>
        """

        # Write the HTML content to the output file
        with open(output_file, 'w') as html_file:
            html_file.write(html_content)

        print(f"HTML file successfully created: {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the conversion
convert_json_to_html(input_file, output_file)
