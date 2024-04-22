
import requests
import csv
from bs4 import BeautifulSoup

count = 1
while(count < 8):
    # Fetch the webpage
    urlBase = "https://neocities.org/browse?sort_by=last_updated&tag=&page="
    url = urlBase + str(count);
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

    # Read existing IDs from the CSV file into a set
    existing_ids = set()
    existing_csv_file = 'test_ids.csv'
    with open(existing_csv_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            existing_ids.add(row[0])  # Assuming IDs are in the first column

    # Append the cleaned IDs to the CSV file, avoiding duplicates
    new_ids = []
    with open(existing_csv_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for clean_id in cleaned_ids:
            if clean_id not in existing_ids:
                writer.writerow([clean_id])
                new_ids.append(clean_id)

    if new_ids:
        print("New cleaned IDs have been added to '{}' file.".format(existing_csv_file))
    else:
        print("No new cleaned IDs were added as they already exist in '{}' file.".format(existing_csv_file))
        
    count = count + 1