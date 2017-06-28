#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Use the BeautifulSoup and requests Python packages to print out a
# list of all the article titles on the New York Times homepage.
# Use code: chcp 65001  in cmd to resolve UnicodeEncodeError

import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

# some requests code here for getting r_html
soup = BeautifulSoup(r_html, "html.parser")

for story_heading in soup.findAll(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())
