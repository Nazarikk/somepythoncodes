#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.kernel.org/")

soup = BeautifulSoup(site.text, 'lxml')

releases_table = soup.find("table", id = "releases")
for tag in releases_table.find_all("tr"):
    name = tag.find("td")
    ver = tag.find("strong")
    print(name.text, ver.text)
