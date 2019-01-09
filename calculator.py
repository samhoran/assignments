def multiply(a,b):
	return a*b
def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def divide(a,b):
	return a/b

print("I'm going to use the calculator functions to multiply 5 and 6")
x = multiply(5,6)
print(x)

def square(a):
	return a**2
def cube(a):
	return a**3
def square_n_times(number, n):
	a = number
	for i in range(n):
		a = a**2
	return a