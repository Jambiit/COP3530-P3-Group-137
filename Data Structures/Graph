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

    # Insertion
    def add_to_taglist(self, site):
        for tag in site.tags:
            self.tag_list[tag].append(site)

    def add_to_sitelist(self, site):
        if site not in self.site_list.keys:
            self.site_list[site]

        for node in self.site_list.keys:
            common_tags = node.tags_in_common(site)
            if common_tags > 0:
                self.site_list[node].append((site, common_tags))

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

site_graph = Graph(input_data)
