import csv
import json

with open('veggies.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)

vegetables = []
for row in rows:
	item = dict(row)
	vegetables.append(item)
print(vegetables)

with open('vegetables.json','w') as f:
	json.dump(vegetables,f)