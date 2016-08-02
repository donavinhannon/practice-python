#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Take the code from the How To Decode A Website exercise (if you didn’t do it
# or just want to play with some different code, use the code from the
# solution), and instead of printing the results to a screen, write the results
# to a txt file. In your code, just make up a name for the file you are saving
# to.
import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text
text = []

# some requests code here for getting r_html
soup = BeautifulSoup(r_html, "html.parser")

for title in soup.findAll(class_="hed"):
    text.append(title.text.strip())

for summary in soup.findAll(class_="dek"):
    text.append(summary.text.replace("/n", " ").strip())

for content in soup.findAll(class_="content drop-cap"):
    if content.span:
        text.append(content.span.text.replace("\n", " ").strip())
    else:
        text.append(content.text.replace("\n", " ").strip())

with open(input("Enter the name of your text _file: ") + ".txt", "w") as open_file:
    open_file.write(str(text))
