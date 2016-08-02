#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Using the requests and BeautifulSoup Python libraries, print to the screen
# the full text of the article on this website:
#    http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print
# out the text to the screen so that you can read the full article without
# having to click any buttons. This will just print the full text of the article
# to the screen. It will not make it easy to read, so next exercise we will
# learn how to write this text to a .txt file.
import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

# some requests code here for getting r_html
soup = BeautifulSoup(r_html, "html.parser")

for title in soup.findAll(class_="hed"):
    print(title.text.strip())

for summary in soup.findAll(class_="dek"):
    print(summary.text.replace("/n", " ").strip())

for content in soup.findAll(class_="content drop-cap"):
    if content.span:
        print(content.span.text.replace("\n", " ").strip())
    else:
        print(content.text.replace("\n", " ").strip())
