"""
Demonstrate screen scraping with BeautifulSoup 

Installed from http://www.crummy.com/software/BeautifulSoup/#Download/ 
Explained at http://www.crummy.com/software/BeautifulSoup/documentation.html
"""

import urllib2
import re
from pprint import pprint
from BeautifulSoup import BeautifulSoup

# read a web page into a big string
page = urllib2.urlopen('http://jon-jacky.github.com/uw_python/winter_2012/index.html').read()

# parse the string into a "soup" data structure
soup = BeautifulSoup(page)

# find all the anchor tags in the soup
anchors = soup.findAll('a')

# find all the anchor tags that link to external web pages
externals = soup.findAll('a',attrs={'href':re.compile('http.*')})

# find all the anchor tags that link to Python files
pythonfiles = soup.findAll('a',attrs={'href':(lambda a: a and a.endswith('.py'))})

# etc. ...
