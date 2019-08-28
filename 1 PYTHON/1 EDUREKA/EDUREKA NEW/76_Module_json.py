import json

data={"name":"akhil","Shares":100,"price":540}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))
print(type(data))
print(data)