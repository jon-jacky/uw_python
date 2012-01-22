"""
scrape.py
Screen-scraping demo: open a page, find and print the first anchor element
"""

import urllib2

url = 'http://jon-jacky.github.com/uw_python/winter_2012/' # course page
page = urllib2.urlopen(url).read()  # now page is one big string
start = page.find('<a ')    # use string method to find first start tag
print page[start:start+60]  # print 60 characters starting at tag


