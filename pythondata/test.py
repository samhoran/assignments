with open('testwrite.txt','w') as f:
	f.write('hello, this is a test file')
	f.write('\n')

with open('testwrite.txt','r') as f:
	full_text = f.read()

print(full_text)