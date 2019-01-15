#Read name.txt into variable my_name
with open('name.txt') as f:
	my_name = f.read()

#Construct greeting.
greeting = 'Hello, my name is ' + my_name + '.'

#Write greeting to a file
with open('hello.txt','w') as f:
	f.write(greeting)