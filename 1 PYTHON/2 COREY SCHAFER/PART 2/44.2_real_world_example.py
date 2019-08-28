"""
pretty common for websites return JSON from their API so that easy to parse

so lets see what grabbing JSON data  from a public API would look like and how we might parse the data 

Yahho Finance API example that converts USA dollars into other currency we can pull down this data and converted the JSON into Python object 
and parse out some information 

so to make the request with WEB Api iam using built in URL lib  module and specifically iam importing URL open from URL lib.request 
 we can also do this by request library

"""

import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/COALINDIA.NS/quote?format=json") as response:
    source = response.read()

print(source)

# now load this string into python object use python.loads method k

data = json.loads(source)

print(json.dumps(data, indent=2))
