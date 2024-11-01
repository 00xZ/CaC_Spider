import json

# Define the input and output file names
input_file = 'db.json'  # Input file path
output_file = 'cleaned_results.json'  # Output file for cleaned JSON lines

# Function to clean and convert JSON strings
def clean_json(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file, open(output_file, 'a', encoding='utf-8') as outfile:
            for line in file:
                # Remove surrounding quotes and unescape the string
                clean_line = line.strip().strip('"')  # Remove quotes
                clean_line = clean_line.encode('utf-8').decode('unicode_escape')  # Unescape unicode
                
                # Load the cleaned line as a JSON object
                try:
                    json_object = json.loads(clean_line)  # Parse the JSON
                    # Write each JSON object as a line in the output file
                    outfile.write(json.dumps(json_object, ensure_ascii=False) + '\n')
                except json.JSONDecodeError:
                    print("Invalid JSON format:", clean_line)

        print(f"Cleaned JSON data has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the cleaning function
clean_json(input_file, output_file)
