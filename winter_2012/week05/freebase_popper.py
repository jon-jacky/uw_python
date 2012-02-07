"""
Freebase demo from Jon Crump
must download freebase module from http://code.google.com/p/freebase-python/

The Karl Popper query in plain English:

"Find me the names and freebase urls of those people who are held to
have been influenced by Karl Popper, and the name, freebase url, date
of birth, religion, nationality, place of birth with its latitude and
longitude, of other people who influenced them."
"""

import freebase
from pprint import pprint
import json

query = [{
  "name": "Karl Popper",
  "guid": None,
  "type": "/influence/influence_node",
  "influenced": [{
    "guid": None,
    "name": None,
    "type": "/influence/influence_node",
    "influenced_by": [{
      "type": "/people/person",
      "guid": None,
      "name": None,
      "date_of_birth": None,
      "nationality": [],
      "religion": [],
      "place_of_birth":[{
        "name": None,
        "/location/location/geolocation": {
          "latitude" : None,
          "longitude" : None
        }
      }]
    }]
  }]
}]

result = freebase.mqlread(query)
pprint(result,indent=1)
