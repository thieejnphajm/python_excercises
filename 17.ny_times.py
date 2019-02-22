#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# The How To Decode A Website exercise was a challenging one, involving many complex pieces of code and two new Python
# modules. When appropaching problems like this one, it helps to develop a plan for the program before executing it.

# Our plan should be as follows:

#     Use the requests library to load the HTML of the page into Python
#     Set up BeautifulSoup to process the HTML
#     Find out which HTML tags contain all the titles
#     Use BeautifulSoup to extract all the titles from the HTML
#     Format them nicely

import requests

from bs4 import BeautifulSoup

base_url = 'http://www.nytimes.com'

r = requests.get(base_url)

soup = BeautifulSoup(r.text, features="html.parser")

for story_heading in soup.find_all(class_="esl82me2"):
    print story_heading.contents


