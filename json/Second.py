import json


with open("/home/anik/lab/python/json/MyFiles.json", "r") as f:
    data = json.load(f)

# print(data)

with open("/home/anik/lab/python/json/MyFiles2.json", "w") as f:
    json.dump(data, f)
    


