import json
import re

# Input and output file paths
input_file = "database.txt"
output_file = "db.json"

# Regular expressions to remove square brackets and ANSI escape codes
brackets_pattern = re.compile(r"\[|\]")
ansi_escape_pattern = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')

# Function to convert text file to JSON
def convert_text_to_json(input_file, output_file):
    # List to hold JSON objects
    json_list = []

    # Read the text file
    with open(input_file, 'r') as file:
        for line in file:
            # Remove ANSI escape codes and square brackets from the line
            cleaned_line = ansi_escape_pattern.sub("", line)
            cleaned_line = brackets_pattern.sub("", cleaned_line.strip())
            
            print(f"Processing cleaned line: {cleaned_line}")  # Debugging output

            # Split the cleaned line into parts
            parts = cleaned_line.split()
            if len(parts) >= 2:
                # Extract components
                url = parts[0]
                status_code = int(parts[1])
                description = " ".join(parts[2:]) if len(parts) > 2 else None

                # Create a dictionary for the JSON object
                entry = {
                    "url": url,
                    "status_code": status_code,
                    "description": description
                }

                # Append to the JSON list
                json_list.append(entry)
            else:
                print(f"Skipping line (unexpected format): {line.strip()}")

    # Write the entire JSON list to the output file as valid JSON
    with open(output_file, 'w') as json_file:
        json.dump(json_list, json_file, indent=4)

    print(f"Data successfully written to {output_file}")

# Run the function to convert text to JSON
convert_text_to_json(input_file, output_file)
