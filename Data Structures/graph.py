import pandas as pd

input_data = pd.read_csv("NeoScraper/small_info.csv")

df = pd.DataFrame(input_data)

# Each site is a node class with sitename, hits, and tags
#
# Each site has list of adjacent sites and a value representing the # of tags shared
#   {site: [(site, 1), (site, 2), (site, 3)]}
# The list will be sorted by hits, each adjacent list will be sorted by # of shared tags
#
# A second tag_list will be created as a way of referencing all sites under a certain tag
#   {tag: [site, site, site]}
# Each list will be sorted by hits

class Graph:
    site_list = {}
    tag_list = {}

    class Site:
        def __init__(self, sitename, hits, tags):
            self.sitename = sitename
            self.hits = hits
            self.tags = tags

        def __eq__(self, other_site):
            if self.sitename == other_site.sitename:
                return True
            else:
                return False

        def print_site(self):
            print(f"{self.sitename}: {self.hits} hits, tags: {self.tags}")

        def tags_in_common(self, site):
            common_tags = 0
            for i in self.tags:
                if i in site.tags:
                    common_tags += 1
            return common_tags
    
    def __init__(self, input_data):
        for row in input_data.rows:
            new_site = self.Site(row["sitename"], row["hits"], row["tags"])
            self.insert(new_site)

    def insert_sorted_taglist(list, site) # Insertion sorted by hits
        inserted = False
        for i, index in enumerate(list):
            if site.hits > i.hits:
                list.insert(index, site)
                inserted = True
        if not inserted:
            list.append(site)

    def insert_sorted_sitelist(list, site, to_insert) # Insertion sorted by tags in common
        inserted = False
        for i, index in enumerate(list):
            insert_tags_in_common = to_insert.tags_in_common(site)
            i_tags_in_common = i.tags_in_common(site)

            if insert_tags_in_common > i_tags_in_common:
                list.insert(index, (to_insert, insert_tags_in_common))
                inserted = True
            if not inserted:
                list.append(site)

    # Insertion
    def add_to_taglist(self, site):
        for tag in site.tags:
            insert_sorted_taglist(self.tag_list[tag], site)

    def add_to_sitelist(self, site):
        if site not in self.site_list.keys:
            self.site_list[site]

        for node in self.site_list.keys:
            common_tags = node.tags_in_common(site)
            if common_tags > 0:
                insert_sorted_sitelist(self.site_list[node], node, site)

    def insert(self, site):
        self.add_to_taglist(site)
        self.add_to_sitelist(site)

    # Searching
    def search_by_name(self, name): # returns single node
        for i in self.site_list:
            if i.sitename == name:
                return i
        print(f"Unable to find site: {name}")
        return

    def search_by_tag(self, tag): # returns list of nodes
        return self.tag_list[tag]

    def print_adjacent_sites(self, name):
        site = search_by_name(name)
        site.print_site()
        print(f"Showing similar results for {name}:")
        for i in self.site_list[site]
            i.print_site()

    def print_taglist_sites(self, tag):
        print(f"Showing results for tag {tag}:")
        for i in self.tag_list[tag]:
            i.print_site()

site_graph = Graph(input_data)
