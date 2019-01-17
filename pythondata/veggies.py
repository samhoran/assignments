import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]



#write row to a CSV
with open("vegetables.csv", "w") as f:
    writer = csv.writer(f)
    #Write header
    writer.writerow(["name", "color","name_length"])
    #Write data
    #loop thru each vegetable
    for vegetable in vegetables:
        writer.writerow([vegetable["name"],vegetable["color"],len(vegetable["name"])])



#I thought this was HW last night so I
#did this, but I'll redo it in class with you now:
#with open('veggies.csv', 'w') as f:
#	writer = csv.writer(f)
#	writer.writerow(['name', 'color', 'name length'])
#	for i in vegetables:
#		writer.writerow([i['name'], i['color'], len(i['name'])])