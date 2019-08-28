'''
import json
print(json.dumps({"name":"Programming",
    "age":22,
    "marks":[90,50,60,70],
    "Object":{
        "color":("red","blue")
    },
    "pass":True}))
print(json.dumps(["1","2"]))
print(json.dumps(("1","2")))
print(json.dumps("Hello World"))
print(json.dumps(100))
print(json.dumps(False))
print(json.dumps(None))
'''


import json

a={
    "name":"Programming",
    "age":22,
    "marks":[90,50,60,70],
    "object":
        {
            "color":("red","color")
        },
    "pass":True
}
    # seperators is replace for , and : and indent is pretty printed purppose how many spaces u want for json object.
# print(json.dumps(a,indent=4,separators=(". "," =")))        # not much preferable

# sort keys parameter is for sort our json according to our alphabetical order
# print(json.dumps(a,indent=4,sort_keys=True))

with open("Work_Json.json",'w') as j:
    j.write(json.dumps(a,indent=2))

# to read the work_json file
with open("Work_json.json","r") as f:
    # print(type(f.read()))
    json_str=f.read()
    json_val=json.loads(json_str)
    print(type(json_val))
    print(json_val["age"])
    print(json_val["name"])
    print(json_val["marks"])