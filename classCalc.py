class calc:

	def sum(self,x,y):
		return x+y
	def difference(self,x,y):
		return x-y
	def product(self,x,y):
		return x*y
	def quot(self,x,y):
		return x/y

x=calc()

while True:
	operation=input("\nOperation from these choices,\nadd\nsub\nmult\ndivide\nexit\n")
	if operation=="exit":
		break
	num1=float(input("num1:\n"))
	num2=float(input("num2:\n"))
	if operation=="add":
		print(x.sum(num1,num2))
	elif operation=="sub":
		print(x.difference(num1,num2))
	elif operation=="mult":
		print(x.product(num1,num2))
	elif operation=="divide":
		print(x.quot(num1,num2))
