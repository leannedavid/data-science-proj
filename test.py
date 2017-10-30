import json
f = open("train.json")
json_parsed = json.load(f)
print(json_parsed[0]["ingredients"])