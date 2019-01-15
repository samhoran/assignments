import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'name length'])
	for i in vegetables:
		writer.writerow([i['name'], i['color'], len(i['name'])])