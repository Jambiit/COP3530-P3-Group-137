import pandas as pd
import re

input_data = pd.read_csv("full_info.csv")

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

        def __str__(self):
            return self.sitename

        def __hash__(self):
            return hash(self.sitename)

        def __eq__(self, other_site):
            if self.sitename == other_site.sitename:
                return True
            else:
                return False

        def print_site(self):
            print(f"{self.sitename}: {self.hits} hits, tags: {self.tags}")

        def site_as_str(self):
            return f"{self.sitename}: {self.hits} hits, tags: {self.tags}"

        def tags_in_common(self, site):
            common_tags = 0
            for i in self.tags:
                if i in site.tags:
                    common_tags += 1
            return common_tags

    def __init__(self, df):
        for index, row in df.iterrows():
            new_site = self.Site(row["sitename"], row["hits"], eval(row["tags"]))
            self.site_list[new_site] = []
            self.add_to_taglist(new_site)
            print(index)
        for site in self.site_list:
            self.add_to_sitelist(site)

    def insert_sorted_sitelist(self, site, to_insert):  # Insertion sorted by tags in common
        insert_tags_in_common = to_insert.tags_in_common(site)
        if not self.site_list[site]:
            self.site_list[site] = [to_insert]

        inserted = False
        for index, i in enumerate(self.site_list[site]):
            i_tags_in_common = i.tags_in_common(site)

            if insert_tags_in_common > i_tags_in_common:
                self.site_list[site].insert(index, to_insert)
                inserted = True
                break
        if not inserted:
            self.site_list[site].append(to_insert)

    # Insertion
    def add_to_taglist(self, site):
        print(site.tags)
        if not site.tags:
            pass
        else:
            for tag in site.tags:
                if tag not in self.tag_list.keys():
                    self.tag_list[tag] = [site]
                else:
                    self.tag_list[tag].append(site)

    def add_to_sitelist(self, site):
        for node in self.site_list:
            common_tags = node.tags_in_common(site)
            if common_tags > 2:
                self.site_list[node].append(site)

    # Searching
    def search_by_name(self, name):  # returns single node
        for i in self.site_list:
            if i.sitename == name:
                return i
        print(f"Unable to find site: {name}")
        return

    def search_by_tag(self, tag):  # returns list of nodes
        return self.tag_list[tag]

    def print_adjacent_sites(self, name):
        site = self.search_by_name(name)
        for i in self.site_list[site]:
            i.print_site()

    def print_taglist_sites(self, tag):
        print(f"Showing results for tag {tag}:")
        for i in self.tag_list[tag]:
            i.print_site()

    def get_sitelist_csv(self):
        df = pd.DataFrame(columns=["site", "adjacent"])
        sites = []
        adjacent_list = []
        for site in self.site_list:
            sites.append(site.sitename)
            adjacent_sites = []
            for i in self.site_list[site]:
                adjacent_sites.append(str(i))
            adjacent_list.append(str(adjacent_sites))
        df["site"] = sites
        df["adjacent"] = adjacent_list
        df.to_csv('sitelist.csv', index=False)

    def get_taglist_csv(self):
        df = pd.DataFrame(columns=["tag", "sites"])
        tag_list = []
        site_list = []
        for tag in self.tag_list:
            tag_list.append(tag)
            sites_in_taglist = []
            for site in self.tag_list[tag]:
                sites_in_taglist.append(str(site))
            site_list.append(str(sites_in_taglist))
        df["tag"] = tag_list
        df["sites"] = site_list
        df.to_csv('tag_list.csv', index=False)


site_graph = Graph(df)
site_graph.get_sitelist_csv()
site_graph.get_taglist_csv()
