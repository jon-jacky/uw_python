"""
json-time.py - demonstrate getting and using JSON formatted data from the web
"""

import urllib2
import json
from pprint import pprint

# urlopen returns a file-like object
data = urllib2.urlopen(
          'http://json-time.appspot.com/time.json')
json_data = json.load(data)
pprint(json_data)
print json_data['datetime']
