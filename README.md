<H1> This is the Neocities search system! </h1>
COP3530 - Project 3

<br/><br/>

## Information and Motivation Behind This Project

Neocities is a web hosting service dedicated to reviving and preserving the era of independent web publishing. As of the end of 2023, Neocities is home to over 700,000 websites. Despite the immense number of websites created and developed by users of Neocities, many of these websites are virtually inaccessible due to the way that the Neocities search engine works.

We find this an issue because one of the main appeals of Neocities is website discovery. A search engine that can effectively collect and display websites in a user-friendly way would be a very useful tool to the explorers of the internet.

To do this we implemented an interactive search bar that allows users to search by name and by tags. The search bar is able to provide suggestions of similar sites based on the tag system included in the data.

<br/><br/>

## How To Access and Use The Search System

You can find our Neocities website at: [ufdsaproject3.neocities.org](ufdsaproject3.neocities.org)

Upon clicking the link you will be brought to the main page of the site where you are given the option to choose a data structure. After clicking a structure you are then prompted to insert a keyword to search.

You may search by the name of an existing Neocities website to find similar websites, or you can search by tag to find all websites of that category!

There is also a tutorial video on how to use the search system at: [https://youtu.be/g14tC7oO35g](https://youtu.be/g14tC7oO35g)

<br/><br/>

## How is the Data Stored?

The Neocities site data is processed and structured in an adjacency list as follows:

A site_list will be created as a way of creating a connection between sites with similar tags:

**{site: [site, site, site]}**

A second tag_list will be created as a way of referencing all sites under a certain tag:

**{tag: [site, site, site]}**

The data is then transformed into a pandas dataframe and written out to a csv file for use in the Neocities search system!

<br/><br/>

## How was this Data Retrieved in the First Place?

We developed a list of 100,000 Neocities websites using Neocities’ built in developer API support and a data scraper that can obtain the necessary data to develop our data structure appropriately named Neoscraper. All websites were pulled from https://neocities.org/browse.

The NeoScraper consists of two main programs. NeoScraper.py collects the IDs of websites and coverts them into cURL addresses. ContentGet takes these converted IDs and uses them to access the JSON files of every website. This obtained information is stored in a CSV file to be moved and processed in our data structures.


