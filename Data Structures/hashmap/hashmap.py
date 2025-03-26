import pandas as pd
import csv


input_data = pd.read_csv("small_info.csv")

df = pd.DataFrame(input_data)


class HashMap:
    site_list = {}
    tag_list = {}
    class Site:
        def __init__(self, site_name, views, hits, created_at, last_updated, tags):
            self.site_name = site_name
            self.views = views
            self.hits = hits
            self.created_at = created_at
            self.last_updated = last_updated
            self.tags = set(tags) if tags else set()

        def update(self, views, hits, last_updated, tags):
            self.views += views
            self.hits += hits
            self.last_updated = last_updated
            if tags:
                self.tags.update(tags)

        def to_dict(self):
            return {
                "Site Name": self.site_name,
                "Views": self.views,
                "Hits": self.hits,
                "Created At": self.created_at,
                "Last Updated": self.last_updated,
                "Tags": list(self.tags)
            }

        def __repr__(self):
            return f"{self.site_name}: Views = {self.views}, Hits = {self.hits}, Created At = {self.created_at}, " \
                   f"Last Updated = {self.last_updated}, Tags = {list(self.tags)}"


    def __init__(self, sitename):
        self.map = {}

    def add(self, site_name, views, hits, created_at, last_updated, tags=None):
        if site_name in self.map:
            self.map[site_name].update(views, hits, last_updated, tags)
        else:
            self.map[site_name] = self.Site(site_name, views, hits, created_at, last_updated, tags)

    def get(self, site_name):
        return self.map.get(site_name, None)

    def display_sorted_by_views(self):
        sorted_sites = sorted(self.map.values(), key=lambda x: x.views, reverse=True)
        print("\nSites sorted by views:")
        for site in sorted_sites:
            print(site)

        with open('sorted_sites.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Views'])
            for site in sorted_sites:
                writer.writerow([site.name, site.views])

        print("\nSites have been written to 'sorted_sites.csv'")

    def to_dataframe(self):
        return pd.DataFrame([site.to_dict() for site in self.map.values()])

    def to_csv(self, filename):
        self.to_dataframe().to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    def from_csv(self, filename):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            site_name = row["Site Name"]
            views = int(row["Views"])
            hits = int(row["Hits"])
            created_at = row["Created At"]
            last_updated = row["Last Updated"]
            tags = set(row["Tags"].strip("[]").replace("'", "").split(", "))
            self.add(site_name, views, hits, created_at, last_updated, tags)
        print(f"Data loaded from {filename}")

    def from_dataframe(self, df):
        for _, row in df.iterrows():
            site_name = row["Site Name"]
            views = int(row["Views"])
            hits = int(row["Hits"])
            created_at = row["Created At"]
            last_updated = row["Last Updated"]
            tags = set(row["Tags"].strip("[]").replace("'", "").split(", "))
            self.add(site_name, views, hits, created_at, last_updated, tags)
        print(f"Data loaded from DataFrame.")

    def from_neocities(self, api_key, requests=None):
        url = "https://neocities.org/api/list"
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for site in data["files"]:
                site_name = site["path"].split("/")[0]
                views = site.get("views", 0)
                hits = site.get("hits", 0)
                created_at = site.get("created_at", "Unknown")
                last_updated = site.get("updated_at", "Unknown")
                tags = ["unknown"]  # Placeholder for tags

                self.add(site_name, views, hits, created_at, last_updated, tags)
            print("Neocities data loaded successfully.")
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")

    def load_sample_data(self):
        sample_data = [
            ("siteA", 1500, 120, "2023-01-10", "2024-03-12", ["technology", "gaming"]),
            ("siteB", 980, 95, "2022-11-05", "2024-03-10", ["art", "design"]),
            ("siteC", 3400, 200, "2021-08-21", "2024-03-11", ["technology", "coding"])
        ]
        sample_df = pd.DataFrame(sample_data, columns=["Site Name", "Views", "Hits", "Created At", "Last Updated", "Tags"])
        self.from_dataframe(sample_df)
        print("Sample data loaded into the hash map.")

df.to_csv("site_views.csv", index=False)
hashmap = HashMap("site_views")
hashmap.from_csv("small_info.csv")
hashmap.to_csv("sorted_sites.csv")

hashmap.display_sorted_by_views()
import pandas as pd
import csv


input_data = pd.read_csv("small_info.csv")

df = pd.DataFrame(input_data)
print(df)

class HashMap:
    site_list = {}
    tag_list = {}
    class Site:
        def __init__(self, site_name, views, hits, created_at, last_updated, tags):
            self.site_name = site_name
            self.views = views
            self.hits = hits
            self.created_at = created_at
            self.last_updated = last_updated
            self.tags = set(tags) if tags else set()

        def update(self, views, hits, last_updated, tags):
            self.views += views
            self.hits += hits
            self.last_updated = last_updated
            if tags:
                self.tags.update(tags)

        def to_dict(self):
            return {
                "Site Name": self.site_name,
                "Views": self.views,
                "Hits": self.hits,
                "Created At": self.created_at,
                "Last Updated": self.last_updated,
                "Tags": list(self.tags)
            }

        def __repr__(self):
            return f"{self.site_name}: Views = {self.views}, Hits = {self.hits}, Created At = {self.created_at}, " \
                   f"Last Updated = {self.last_updated}, Tags = {list(self.tags)}"


    def __init__(self, sitename):
        self.map = {}

    def add(self, site_name, views, hits, created_at, last_updated, tags=None):
        if site_name in self.map:
            self.map[site_name].update(views, hits, last_updated, tags)
        else:
            self.map[site_name] = self.Site(site_name, views, hits, created_at, last_updated, tags)

    def get(self, site_name):
        return self.map.get(site_name, None)

    def display_sorted_by_views(self):
        sorted_sites = sorted(self.map.values(), key=lambda x: x.views, reverse=True)
        print("\nSites sorted by views:")
        for site in sorted_sites:
            print(site)

        with open('sorted_sites.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Views'])
            for site in sorted_sites:
                writer.writerow([site.name, site.views])

        print("\nSites have been written to 'sorted_sites.csv'")

    def to_dataframe(self):
        return pd.DataFrame([site.to_dict() for site in self.map.values()])

    def to_csv(self, filename):
        self.to_dataframe().to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    def from_csv(self, filename):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            site_name = row["Site Name"]
            views = int(row["Views"])
            hits = int(row["Hits"])
            created_at = row["Created At"]
            last_updated = row["Last Updated"]
            tags = set(row["Tags"].strip("[]").replace("'", "").split(", "))
            self.add(site_name, views, hits, created_at, last_updated, tags)
        print(f"Data loaded from {filename}")

    def from_dataframe(self, df):
        for _, row in df.iterrows():
            site_name = row["Site Name"]
            views = int(row["Views"])
            hits = int(row["Hits"])
            created_at = row["Created At"]
            last_updated = row["Last Updated"]
            tags = set(row["Tags"].strip("[]").replace("'", "").split(", "))
            self.add(site_name, views, hits, created_at, last_updated, tags)
        print(f"Data loaded from DataFrame.")

    def from_neocities(self, api_key, requests=None):
        url = "https://neocities.org/api/list"
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for site in data["files"]:
                site_name = site["path"].split("/")[0]
                views = site.get("views", 0)
                hits = site.get("hits", 0)
                created_at = site.get("created_at", "Unknown")
                last_updated = site.get("updated_at", "Unknown")
                tags = ["unknown"]  # Placeholder for tags

                self.add(site_name, views, hits, created_at, last_updated, tags)
            print("Neocities data loaded successfully.")
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")

    def load_sample_data(self):
        sample_data = [
            ("siteA", 1500, 120, "2023-01-10", "2024-03-12", ["technology", "gaming"]),
            ("siteB", 980, 95, "2022-11-05", "2024-03-10", ["art", "design"]),
            ("siteC", 3400, 200, "2021-08-21", "2024-03-11", ["technology", "coding"])
        ]
        sample_df = pd.DataFrame(sample_data, columns=["Site Name", "Views", "Hits", "Created At", "Last Updated", "Tags"])
        self.from_dataframe(sample_df)
        print("Sample data loaded into the hash map.")

df.to_cvs("site_views.csv", index=False)
hashmap = HashMap("site_views")
hashmap.from_csv("full_info.csv")
hashmap.to_csv("sorted_sites.csv")

hashmap.display_sorted_by_views()
import pandas as pd
import csv


input_data = pd.read_csv("small_info.csv")

df = pd.DataFrame(input_data)
print(df)

class HashMap:
    site_list = {}
    tag_list = {}
    class Site:
        def __init__(self, site_name, views, hits, created_at, last_updated, tags):
            self.site_name = site_name
            self.views = views
            self.hits = hits
            self.created_at = created_at
            self.last_updated = last_updated
            self.tags = set(tags) if tags else set()

        def update(self, views, hits, last_updated, tags):
            self.views += views
            self.hits += hits
            self.last_updated = last_updated
            if tags:
                self.tags.update(tags)

        def to_dict(self):
            return {
                "Site Name": self.site_name,
                "Views": self.views,
                "Hits": self.hits,
                "Created At": self.created_at,
                "Last Updated": self.last_updated,
                "Tags": list(self.tags)
            }

        def __repr__(self):
            return f"{self.site_name}: Views = {self.views}, Hits = {self.hits}, Created At = {self.created_at}, " \
                   f"Last Updated = {self.last_updated}, Tags = {list(self.tags)}"


    def __init__(self, sitename):
        self.map = {}

    def add(self, site_name, views, hits, created_at, last_updated, tags=None):
        if site_name in self.map:
            self.map[site_name].update(views, hits, last_updated, tags)
        else:
            self.map[site_name] = self.Site(site_name, views, hits, created_at, last_updated, tags)

    def get(self, site_name):
        return self.map.get(site_name, None)

    def display_sorted_by_views(self):
        sorted_sites = sorted(self.map.values(), key=lambda x: x.views, reverse=True)
        print("\nSites sorted by views:")
        for site in sorted_sites:
            print(site)

        with open('sorted_sites.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Views'])
            for site in sorted_sites:
                writer.writerow([site.site_name, site.views])

        print("\nSites have been written to 'sorted_sites.csv'")

    def to_dataframe(self):
        return pd.DataFrame([site.to_dict() for site in self.map.values()])

    def to_csv(self, filename):
        self.to_dataframe().to_csv(filename, index=False)
        print(f"Data saved to {filename}")

    def from_csv(self, filename):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            site_name = row["Site Name"]
            views = int(row["Views"])
            hits = int(row["Hits"])
            created_at = row["Created At"]
            last_updated = row["Last Updated"]
            tags = set(row["Tags"].strip("[]").replace("'", "").split(", "))
            self.add(site_name, views, hits, created_at, last_updated, tags)
        print(f"Data loaded from {filename}")

    def from_dataframe(self, df):
        for _, row in df.iterrows():
            site_name = row["Site Name"]
            views = int(row["Views"])
            hits = int(row["Hits"])
            created_at = row["Created At"]
            last_updated = row["Last Updated"]
            tags = set(row["Tags"].strip("[]").replace("'", "").split(", "))
            self.add(site_name, views, hits, created_at, last_updated, tags)
        print(f"Data loaded from DataFrame.")

    def from_neocities(self, api_key, requests=None):
        url = "https://neocities.org/api/list"
        headers = {"Authorization": f"Bearer {api_key}"}

        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            for site in data["files"]:
                site_name = site["path"].split("/")[0]
                views = site.get("views", 0)
                hits = site.get("hits", 0)
                created_at = site.get("created_at", "Unknown")
                last_updated = site.get("updated_at", "Unknown")
                tags = ["unknown"]  # Placeholder for tags

                self.add(site_name, views, hits, created_at, last_updated, tags)
            print("Neocities data loaded successfully.")
        else:
            print(f"Failed to fetch data: {response.status_code} - {response.text}")

    def load_sample_data(self):
        sample_data = [
            ("siteA", 1500, 120, "2023-01-10", "2024-03-12", ["technology", "gaming"]),
            ("siteB", 980, 95, "2022-11-05", "2024-03-10", ["art", "design"]),
            ("siteC", 3400, 200, "2021-08-21", "2024-03-11", ["technology", "coding"])
        ]
        sample_df = pd.DataFrame(sample_data, columns=["Site Name", "Views", "Hits", "Created At", "Last Updated", "Tags"])
        self.from_dataframe(sample_df)
        print("Sample data loaded into the hash map.")

df.to_csv("site_views.csv", index=False)

hashmap = HashMap("site_views")
hashmap.from_csv("full_info.csv")

hashmap.to_csv("sorted_sites.csv")
hashmap.display_sorted_by_views()
