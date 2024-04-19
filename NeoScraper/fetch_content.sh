#!/bin/bash

# Function to fetch content from a URL and save it to a file
fetch_url_content() {
    local url=$1
    local output_file=$2
    curl -s "$url" -o "$output_file"
}

# Function to process JSON content and extract information
process_json_content() {
    local input_file=$1
    jq -r '.info.sitename, .info.views, .info.hits, .info.created_at, .info.last_updated, (.info.tags | join(","))' "$input_file"
}

# Process URLs from a CSV file
process_urls_from_csv() {
    local csv_file=$1
    while IFS=, read -r url; do
        # Generate a filename based on the URL
        output_file="$(echo "$url" | tr -d '\r' | sed 's/[^a-zA-Z0-9]/_/g').txt"
        
        # Fetch content from the URL and save it to a temporary file
        temp_file=$(mktemp)
        fetch_url_content "$url" "$temp_file"
        
        # Process the JSON content and print the extracted information
        process_json_content "$temp_file"
        
        # Clean up temporary file
        rm "$temp_file"
    done < "$csv_file"
}

# Check if a CSV file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file>"
    exit 1
fi

# Check if the provided CSV file exists
csv_file="$1"
if [ ! -f "$csv_file" ]; then
    echo "Error: CSV file '$csv_file' not found."
    exit 1
fi

# Process URLs from the CSV file
process_urls_from_csv "$csv_file" | awk 'BEGIN { print "sitename,views,hits,created_at,last_updated,tags" } { print }' > output.csv

echo "Content from all URLs processed and saved to output.csv"
