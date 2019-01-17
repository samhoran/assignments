#Import packages
import csv
import json
from pprint import pprint

#Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = [dict(row) for row in reader] # Convert Ordered Dict to regular dict (python 3.6 or higher)

#group veggies by color in dictionary vegetables_by_color
vegetables_by_color = {}
for veg in vegetables:
    color = veg['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(veg)
    else:
        vegetables_by_color[color] = [veg]

pprint(vegetables_by_color)

#Write the veggies to a json file
with open('vegetables_by_color.json', 'w') as f:
    json.dump(vegetables_by_color, f, indent = 2)