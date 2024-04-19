import json
import csv
import requests

def get_info_from_curl(curl_url):
    # Make a GET request to the cURL URL
    response = requests.get(curl_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract 'info' part of JSON
        info = data.get('info', {})
        if 'domain' in info:
            del info['domain']
        return info
    else:
        print(f"Failed to retrieve data from {curl_url}")
        return None

def process_curls(input_csv, output_csv):
    with open(input_csv, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        info_list = []
        for row in reader:
            curl_url = row[0]
            info = get_info_from_curl(curl_url)
            if info:
                info_list.append(info)
    
    # Write the extracted data to a CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['sitename', 'views', 'hits', 'created_at', 'last_updated', 'tags'])
        writer.writeheader()
        for info in info_list:
            writer.writerow(info)
    
    print(f"Data saved to {output_csv}")

# Example usage
input_csv = "random_ids.csv"
output_csv = "small_random_info.csv"
process_curls(input_csv, output_csv)
