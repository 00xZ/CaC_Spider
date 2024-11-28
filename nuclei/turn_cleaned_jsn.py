import json # parsing the db into json due to lack of skill or laziness, im not sure which one yet
import re

# Define the path to your vuln_cleaned.db file
input_file = 'vuln_cleaned.db'
output_file = 'vuln_cleaned_with_severity.json'

# Initialize an empty dictionary to store CVE data
cve_data = {}

# Regular expression for matching general CVE and URL data
cve_regex = r'\[([^\]]+)\] \[([^\]]+)\] \[([^\]]+)\] ([^\[]+)'

# Regular expression for extracting usernames from WordPress user enumeration
wp_usernames_regex = r'\[wp-user-enum:usernames\] \[([^\]]+)\] \[([^\]]+)\] (.+)'

# Open the vuln_cleaned.db file and parse each line
with open(input_file, 'r') as file:
    for line in file:
        # Check for WordPress user enumeration pattern
        wp_match = re.match(wp_usernames_regex, line)
        if wp_match:
            cve_id = wp_match.group(1)  # Extract the CVE ID (e.g., [wp-user-enum:usernames])
            severity = wp_match.group(2)  # Extract the severity (low, medium, high)
            url = wp_match.group(3).split(' ')[0]  # Extract the URL
            usernames = wp_match.group(3).split(' ', 1)[1] if len(wp_match.group(3).split(' ', 1)) > 1 else None  # Extract usernames

            # Print debug info to check if usernames are correctly extracted
            print(f"Debug - WordPress URL: {url}, Usernames: {usernames}")

            # Initialize the CVE entry if it doesn't exist
            if cve_id not in cve_data:
                cve_data[cve_id] = {
                    'severity': severity,
                    'urls': []
                }

            # Add the URL and associated info (usernames) to the list of URLs under this CVE
            cve_data[cve_id]['urls'].append({
                'url': url,
                'info': f'Usernames: {usernames}' if usernames else None
            })

        # General CVE match (e.g., [CVE-2023-48795], [javascript], [medium])
        else:
            match = re.match(cve_regex, line)
            if match:
                cve_id = match.group(1)  # Extract the CVE ID
                severity = match.group(3)  # Extract the severity (low, medium, high)
                url = match.group(4).split(' ')[0]  # Extract the URL, trimming extra data
                info = match.group(4).split(' ', 1)[1] if len(match.group(4).split(' ', 1)) > 1 else None  # Extract additional info if present

                # Initialize the CVE entry if it doesn't exist
                if cve_id not in cve_data:
                    cve_data[cve_id] = {
                        'severity': severity,
                        'urls': []
                    }

                # Add the URL and associated info to the list of URLs under this CVE
                cve_data[cve_id]['urls'].append({
                    'url': url,
                    'info': info
                })

# Write the resulting data to a JSON file
with open(output_file, 'w') as json_file:
    json.dump(cve_data, json_file, indent=4)

print(f'Converted data saved to {output_file}')
