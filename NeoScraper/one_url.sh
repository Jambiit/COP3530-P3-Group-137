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
    local output_file=$2
    jq -r '.info.sitename, .info.views, .info.hits, .info.created_at, .info.last_updated, .info.tags[]' "$input_file" > "$output_file"
}

# Loop through the list of URLs provided as arguments
for url in "$@"; do
    # Generate a filename based on the URL
    output_file="$(echo "$url" | tr -d '\r' | sed 's/[^a-zA-Z0-9]/_/g').txt"
    
    # Fetch content from the URL and save it to a temporary file
    temp_file=$(mktemp)
    fetch_url_content "$url" "$temp_file"
    
    # Process the JSON content and save the extracted information to a file
    process_json_content "$temp_file" "$output_file"
    
    echo "Content from $url processed and saved to $output_file"
    
    # Clean up temporary file
    rm "$temp_file"
done