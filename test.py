import json
import pandas as pd
f = open("train.json")
json_parsed = json.load(f)
pd_json = read_json(json_parsed)

print(pd_json)