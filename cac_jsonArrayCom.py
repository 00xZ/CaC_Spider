import json

# Input JSON file with multiple arrays
input_file = "cac_results.json"
# Output corrected JSON file
output_file = "corrected_cac_results.json"

def combine_json_arrays(input_file, output_file):
    combined_data = []

    try:
        # Read the file line by line
        with open(input_file, 'r') as file:
            for line in file:
                try:
                    # Parse each JSON array
                    data = json.loads(line.strip())
                    if isinstance(data, list):  # Ensure it's a list
                        combined_data.extend(data)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON line: {line.strip()}")

        # Write the combined data to the output file
        with open(output_file, 'w') as file:
            json.dump(combined_data, file, indent=4)

        print(f"Combined JSON file created: {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to combine JSON arrays
combine_json_arrays(input_file, output_file)
