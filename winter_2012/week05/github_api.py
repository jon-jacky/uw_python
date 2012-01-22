"""
github-api.py

Demonstrate getting and using JSON formatted data from GitHub
Based on example at http://develop.github.com/p/repo.html

Here we retrieve the names of all of one particular users' repositories,
that can also be viewed on the page at https://github.com/jon-jacky
"""

import urllib2
import json
from pprint import pprint

# this user has several repos. URL here is a GitHub API call
url = 'http://github.com/api/v2/json/repos/show/jon-jacky'
handle = urllib2.urlopen(url)
data = json.load(handle)

pprint(data) # show all the data for all the repos
print        # leave some space
print 

# We see data is a big dictionary with one key, u'repositories'
# whose value is a list of dictionaries, one for each repo
# in each of these dictionaries, look up repo name at key u'name'

names = [ r[u'name'] for r in data[u'repositories'] ]
pprint(names)

