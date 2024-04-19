
import requests
import csv
from bs4 import BeautifulSoup

# Fetch the webpage
url = 'https://neocities.org/browse'
response = requests.get(url)
html_content = response.text

# Parse the HTML snippet
soup = BeautifulSoup(html_content, 'html.parser')

# Find all list items
list_items = soup.find_all('li')

# Extract and clean the id attribute of each list item
cleaned_ids = [];
for item in list_items:
    item_id = item.get('id')
    if item_id:
        clean_id = item_id.replace("username_", "https://neocities.org/api/info?sitename=")
        print("Cleaned ID:", clean_id)
        cleaned_ids.append(clean_id)

    else:
        print("No ID attribute found for this hlist item.")

# Output the cleaned IDs to a CSV file    
with open('cleaned_ids.csv', 'w', newline='') as csvfile: #CHANGE OUTPUT FILE HERE
    writer = csv.writer(csvfile)
    #writer.writerow(['Cleaned IDs']) #don't need a tile
    for clean_id in cleaned_ids:
        writer.writerow([clean_id])

print("Cleaned IDs have been written to 'cleaned_ids.csv' file.")