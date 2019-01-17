#SAM AND NURLAN

#import packages
import csv
import json
from pprint import pprint

#Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)


#Loop through vegetables and filter down to only green vegtables using a whitelist.
whitelist=['green']
green_vegetables = []
for vegetable in vegetables:
    if vegetable['color'] in whitelist:
        green_vegetables.append(vegetable)

#Print veggies to terminal
pprint(green_vegetables)

#Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', 'w') as f:
    json.dump(green_vegetables, f, indent = 2)

#Write to a CSV instead
with open('greenveggies.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['name','color','name_length'])
	for v in green_vegetables:
		writer.writerow([v['name'],v['color'],v['name_length']])