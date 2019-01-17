import csv
import json

#Read CSV file (vegetables.csv)
with open('vegetables.csv','r') as f:
	reader = csv.DictReader(f)
	vegetables = [dict(row) for row in reader] #Convert ordered dict to list of dict

#Print variable vegetables
print(vegetables)

#Write JSON file (vegetables.json)
with open('vegetables.json','w') as f:
	json.dump(vegetables,f,indent=2)