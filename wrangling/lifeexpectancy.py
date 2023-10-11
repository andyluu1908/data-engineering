import csv
import json

csvfile = open("lifeexpectancydata.csv", "r")
reader = csv.DictReader(csvfile)

json_data = open("lifeexpectancydata.json").read()
data = json.loads(json_data)

for row in data:
  print(row)