def sum(x,y):
	return x+y
	return x-y
def product(x,y):
	return x*y
def quotient(x,y):
	return x/y
	
	
	num2=float(input("Enter number two: \n"))
	if operation=="add":
		print(sum(num1,num2))
	elif operation=="sub":
		print(difference(num1,num2))
	elif operation=="mult":
		print(product(num1,num2))
	elif operation=="divide":
		print(quotient(num1,num2))
