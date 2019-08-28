"""
in our previous tutorial we see this for json topic

use json.loads for load JSON string into Python object
use json.dumps for load Python object into JSON string


now let us see how to load JSON files into PYTHON objects and write those python objects back into JSON Files
"""

"""
i want to load states.json into python object i use json.load method k  

load 												vs                                       loads
load method loads a file into python object                                                  loads the json string to python object 

dump                                                vs                                       dumps
converts the data into JSON file                                                             converts the data into json string
"""

import json

# load json file into python object to open a file in python states.json

with open("states.json") as f:
    data = json.load(f)

for state in data["states"]:
    # print(state)
    # it is python object so we are able to et the data like this
    # print(state["name"], state["abbreviation"])

    # now to load python object into JSON file k with remove of area code got it understand
    del state["area_codes"]
with open("new_states.json", "w") as f:
    json.dump(data, f, indent=3)
